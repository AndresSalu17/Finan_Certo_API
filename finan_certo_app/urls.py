"""
URL configuration for finan_certo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from rest_framework import routers

from finan_certo.views import FinancasUsuarioViewSet, LoginViewSet, UserViewSet, UsuarioMetaViewSet

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

router = routers.DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'financasusuario', FinancasUsuarioViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'usuariometa', UsuarioMetaViewSet, basename='usuariometa')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('api/gettoken/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
