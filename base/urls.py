from django.urls import path
from . import views

urlpatterns= [
    path('lobby', views.lobby, name='lobby'),
    path('room/', views.room, name='cuarto'),
    path('get_token/', views.getToken, name='get_token'),
    path('contenido/', views.contenido, name='contenido'),
    path('pruebaUno/', views.pruebaUno, name='pruebaUno'),
    path('contenidoDos/', views.pruebaDos, name='contenidoDos'),
    path('inicio/', views.inicio, name='inicio'),
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
    
]
