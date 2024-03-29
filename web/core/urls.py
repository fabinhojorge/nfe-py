"""nfe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, re_path
from .views import nfe_sync_v1, nfe_find_v1

urlpatterns = [
    path('v1/nfe/sync/', nfe_sync_v1, name='nfe_sync'),
    re_path('v1/nfe/find/(?P<access_key>[0-9]{44})', nfe_find_v1, name='nfe_find'),
]
