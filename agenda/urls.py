"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core.views import tela_principal,matriculasubmit,tela_login,sair
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tela_principal/', tela_principal, name= 'tela_principal'),
    path('submit_matricula/', matriculasubmit, name= 'matriculasubmit' ),
    path('tela_login/', tela_login, name= 'tela_login' ),
    path('logout/', sair, name='logout'),
]
