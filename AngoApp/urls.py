"""AngoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Main import views as MainViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',MainViews.HomePage,name='home'),
    url(r'^about',MainViews.AboutUs,name='about'),
    url(r'^portofolio',MainViews.portofolio,name='portofolio'),
    url(r'^process',MainViews.process,name='process'),
    url(r'^services',MainViews.services,name='services'),
    url(r'^contact',MainViews.contact,name='contact'),

   
    url(r'^admin/', admin.site.urls),
    url(r'^Administrator/(?P<Administrator_name>\D+)',MainViews.AdministratorView,name='Administrator_view'),
    url(r'^Client/(?P<Client_name>\D+)',MainViews.ClientsView,name='jose'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
