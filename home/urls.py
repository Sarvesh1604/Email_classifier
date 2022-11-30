"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from pages.views import home_view, form_view
from Add_Emails.views import add_emails_view
from Display_Emails.views import show_emails_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path('form/', form_view, name='form'),
    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', add_emails_view.as_view(template_name='add_emails.html'), name='add_emails'),
    # path('', show_emails_view.as_view(template_name='show_emails.html'), name='show_emails'),
    path('add_emails/', add_emails_view, name='add_emails'),
    path('show_emails/', show_emails_view, name='show_emails'),
]
