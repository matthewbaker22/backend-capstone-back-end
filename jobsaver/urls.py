"""jobsaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from jobsaverapi.views import *
from jobsaverapi.models import *
from django.conf import settings
from django.conf.urls.static import static
from jobsaverapi.views import login_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'jobs', Jobs, 'job')
router.register(r'status', Statuses, 'status')
router.register(r'job_status', Job_Statuses,'job_status')
router.register(r'user', Users, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', login_user),
    path('register/', register_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
