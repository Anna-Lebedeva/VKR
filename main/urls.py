from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^', views.Index.as_view(), name='index'),
    url(r'^login/$', views.CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.auth_logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^about/', views.About.as_view(), name='about'),
]
