"""firstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from firstpro.views import home

app_name = (
    'posts',
    'user_info',
    'newsletters',
    'erfan_portfolio',
    
)

urlpatterns = [

    # Basic URLS
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # App URLS
    path('posts/', include('posts.urls')),
    path('user-info/', include('user_info.urls')),
    path('portfoilo/',include('erfan_portfolio.urls')),
    path('newsletter/', include('newsletters.urls')),
    path('comments/', include('comments.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
