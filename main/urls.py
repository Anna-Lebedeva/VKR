from django.conf.urls import url
from django.urls import path
from .views import index, about, user_login

urlpatterns = [
    path('', index, name='index'),
    url(r'^login/$', user_login, name='login'),
    path('about/', about, name='about'),
    path('account/', about, name='account'),
]
