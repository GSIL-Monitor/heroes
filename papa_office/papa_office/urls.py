"""cobraWeb URL Configuration

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
from papa_office import view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello', view.hello),
    url(r'^$', view.index),
    url(r'^login', view.login),
    url(r'^register', view.register),
    url(r'^rsubmit', view.registerSubmit),
    url(r'^myview', view.my_view),
    url(r'^email-manager', view.my_view),
    url(r'^remail', view.receiveEmail),
    url(r'^echartsExample',view.echartsExample),
    url(r'^chartjs',view.chartjs),
    url(r'^morris',view.morris),
    url(r'^flot',view.flot),
    url(r'^inline',view.inline),
    url(r'^wordCloud',view.wordCloud),
]
#urlpatterns += staticfiles_urlpatterns()
