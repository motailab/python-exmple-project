from django.conf.urls import url
from TemplateApp import views

app_name = 'TemplateApp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative' ),
    url(r'^other/', views.other, name='other')
]