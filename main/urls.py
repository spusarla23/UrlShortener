from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten_post, name='shorten_post'),
    path('shorten', views.shorten_post, name='shorten_post'),
    path('shorten/<str:url>', views.shorten_post, name='shorten_post'),
    path('<str:url_hash>', views.redirect_hash, name='redirect_hash'),
]
