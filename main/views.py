from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import service
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .webform import URLForm

# Create your views here.
def index(request):
    form = URLForm()
    return render(request, 'main/url_shortener.html', {'form': form})

# method to shorten the url
def shorten_post(request):
    #Django URL mapping only works with path parameters and not with POST. So
    #get the URL from POST and pass it to the path
        if request.method == 'POST':
            form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            print(url)
        try:
            shortened_url_hash = service.shorten(url)
            shortened_url = request.build_absolute_uri(reverse('redirect_hash', args=[shortened_url_hash]))
            print(shortened_url)
        # return HttpResponse(f'Shortened URL : <a href="{shortened_url}">{shortened_url}</a>')
        # return render(request, 'main/url_shortener.html', {'shortened_url': shortened_url})
            return JsonResponse({'shortened_url': shortened_url})
        except Exception as e:
            return JsonResponse({'error_message': f'Error: {e}'}, status=500)
        return JsonResponse({'error_message': 'Invalid request'}, status=400)

# method to get the original url from hash
def redirect_hash(request, url_hash):
   try:
    orig_url = service.load_url(url_hash).orig_url
    if not orig_url.startswith(('http://', 'https://')):
            orig_url = 'http://' + orig_url
    # print(orig_url)
    return redirect(orig_url)
   except service.Question.DoesNotExist:
       return HttpResponse(status=400, content="No URL provided")

def shorten(request, url):
    try:
        #Initialize the shortener
        #shortener = pyshorteners.Shortener()

       # testurl = 'google.com'
        #shorten the url with chilp.it api 
       # shortened_url = shortener.chilpit.short(url)  

        shortened_url_hash = service.shorten(url)
        shortened_url = request.build_absolute_uri(reverse('redirect_hash', args=[shortened_url_hash]))
        
       # return HttpResponse(f'Shortened URL : <a href="{shortened_url}">{shortened_url}</a>')
        return render(request, 'main\link.html', {'shortened_url': shortened_url})
       # return JsonResponse('shortened_url': shortened_url)
       # return HttpResponse(shortened_url)
    except Exception as e:
        return HttpResponse(status=500, content=str(e))