"""
URL configuration for taehasite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from taehasite.views import HomeView, servicesView, portfolioView, aboutView, teamView, contactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('services/', servicesView.as_view(), name='services'),
    path('portfolio/', portfolioView.as_view(), name='portfolio'),
    path('about/', aboutView.as_view(), name='about'),
    path('team/', teamView.as_view(), name='team'),
    path('contact/', contactView.as_view(), name='contact')
]
