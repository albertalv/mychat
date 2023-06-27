from django.urls import path
from . import views
from .views import vista, vistaCheckout, vistaExitoso, subirVideo, vistaInicio
from .views import room
urlpatterns= [
    path('lobby/', vista.as_view(), name='lobby'),
    #path('room/', views.room, name='cuarto'),
    path('get_token/', views.getToken, name='get_token'),
    path('contenido/', views.contenido, name='contenido'),
    path('pruebaUno/', views.pruebaUno, name='pruebaUno'),
    path('contenidoDos/', views.pruebaDos, name='contenidoDos'),
    path('inicio/', vistaInicio.as_view(), name='inicio'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.exit, name='exit'),
    path('loginDos/', views.custom_login, name="loginDos"),
    path('accounts/admin_profile/', views.admin_profile, name='admin_profile'),
    path('register/',views.register, name='register'),
    path('crud_user/', views.crudInformacion, name='crud_user'),
    path('my_tokens/', views.myTokens, name ="my_tokens"),
    path('my_money/', views.myMoney, name='my_money'),
    path('buzon/', views.buzon, name= 'buzon'),
    path('validacion/', views.validacion, name='validacion'),
    path('resolverDenuncia/', views.resolverDenuncia, name="resolverDenuncia"),
    path('crearCategoria/', views.crearCategorias, name="crearCategoria"),
    path('tokens/', views.tokens, name="tokens"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('categorias/', views.categorias, name="categorias"),
    path('canal/', views.previo, name='canal'),
    path('canal/<str:room_name>/', room.as_view(), name='room'),
    path('checkout/<int:paquete_id>/', vistaCheckout.as_view(), name='checkout'),
    path('graciasPorTuCompra/', vistaExitoso.as_view(), name ="exitoso"),
    path('subirVideo/', subirVideo.as_view(), name = 'subirVideo' ), 
    
]
