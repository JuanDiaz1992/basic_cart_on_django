"""
URL configuration for locallibrary project.

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
from users.views import viewsUsers, createNewUser
from productos.views import viewProducts, agregar_producto, viewCar, deleteCart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usersAdmin/', viewsUsers, name="usersAdmin"),
    path('createNewUser/', createNewUser, name="createNewUser"),
    path('viewProducts/', viewProducts, name="viewProducts"),
    path('agregar_producto/<int:id>/', agregar_producto, name='agregar_producto'),
    path('viewCar/', viewCar, name='viewCar'),
    path('deleteCart/',deleteCart, name='deleteCart')
]
