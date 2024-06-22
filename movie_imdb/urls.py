"""
URL configuration for movie_imdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from django.contrib import admin
from django.urls import path, include

from core.views import home


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # Add other views as needed
    # path('community/', community.as_view, name='community'),
    # path('discovery/', discovery.as_view, name='discovery'),
    # path('coming_soon/', coming_soon.as_view, name='coming_soon'),
    # path('profile/', profile.as_view, name='profile'),
    # path('friends/', friends.as_view, name='friends'),
    # path('media/', media.as_view, name='media'),
    # path('settings/', settings.as_view, name='settings'),
    # path('logout/', logou.as_view, name='logout'),
]
