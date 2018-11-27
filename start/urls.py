from django.conf.urls import url
from django.urls import path
from start import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^appraise', views.appraise, name='appraise'),
    url(r'^showall', views.showall, name='showall'),

]