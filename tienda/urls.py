from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .  import views


urlpatterns = [
    path('',views.home, name='inicio' ),
    path('Carrito/',views.carrito, name='Carrito' ),
    path('Clasica/',views.clasica, name='Clasica' ),
    path('Contacto/',views.contacto, name='Contacto' ),
    path('login/',views.ingresar, name='ingresar' ),
    path('Jazz/',views.jazz, name='Jazz' ),
    path('Nosotros/',views.nosotros, name='Nosotros' ),
    path('Rock/',views.rock, name='Rock' ),
    path('registro/',views.registro, name='registro' ),
    path('agregar-producto', views.agregar_producto, name = 'agregar_producto'),
    path('listar-producto', views.listar_producto, name = 'listar_producto'),
    path('modificar-producto/<id>/', views.modificar_producto, name = 'modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name = 'eliminar_producto'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]
