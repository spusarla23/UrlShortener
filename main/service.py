import random
import string
from django.utils import timezone

from .models import Question

def shorten(url):
    #save the orig_url and its hash in the database
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Question(orig_url=url, hash=random_hash, creation_date=timezone.now())
    #print(mapping.__dict__)
    mapping.save()
    return random_hash

def load_url(url_hash):
    #print(Question.objects.get(hash=url_hash))
    #get the original url for url_hash
    return Question.objects.get(hash=url_hash)
