from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('' , views.home , name='home'),
    path('register/' , views.register , name='register'),
    path('log/' , views.log , name='log'),
    path('logout_form/' , views.logout_form , name='logout_form'),

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)