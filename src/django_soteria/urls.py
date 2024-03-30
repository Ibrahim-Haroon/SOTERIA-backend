"""
URL configuration for django_soteria project.

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
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def root_view(
        request
) -> HttpResponse:  # pragma: no cover
    """
    @rtype: HttpResponse
    @param request: request object
    @return: response for root view
    """
    return HttpResponse("Hello! You're at the root of the SOTERIA server.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),
    path('chat_endpoint/', include('src.chat_endpoint.urls')),
    path('chat_stream/', include('src.chat_stream.urls')),
]
