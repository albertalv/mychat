from typing import Any
from django import http
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from agora_token_builder import RtcTokenBuilder
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from .forms import LoginForm
from .forms import CustomUserCreationForm
from .models import Stream
from .models import Estatus
import random
import time 
from .models import UserProfile
import json
from django.contrib.auth.models import User
from .models import Paquetes
from django.http import HttpResponseForbidden
import base64
import http.client
from .models import videos
import boto3
import base64
from django.core.exceptions import ObjectDoesNotExist
connected = False
# Create your views here.
def getToken(request):
    appId = "380a5ca3bd4f4cd09bd565211dd8aa02"
    appCertificate = "6f4ecbd86ba6480cab672f0c3f6d86ca"
    channelName = request.GET.get("channel")
    uid = random.randint(0,100)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    Stream.objects.filter(channel=channelName).delete()
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    stream_obj = Stream(appId= appId, channel = channelName, token = token, uid=uid)
    stream_obj.save()
    return JsonResponse({"token": token, "uid": uid}, safe=False)

class vista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        saldo= request.GET.get('tokens', None)
        context = {'tokens': tokens}
        context = {
            'tokens': user_profile.tokens, 
            'saldo': saldo,
        }
        return render(request, 'base/lobby.html', context)
    
    """def post(self, request): 
        channel = request.POST.get('channel')
        estado = request.POST.get('estado')
        Estatus.objects.filter(channel=channel).delete()
        objeto = Estatus(channel=channel, estado=estado)
        objeto.save()
        return HttpResponse('Operación exitosa')"""
    
    def put(self, request):
        data = json.loads(request.body)
        tokens = int(data.get('tokens'))
        host_id = data.get('hostId')
        
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            host_profile = UserProfile.objects.get(user_id=host_id)
            
            if tokens > user_profile.tokens:
                return HttpResponse('No tienes suficientes tokens', status=400)
            
            user_profile.tokens -= tokens
            host_profile.tokens += tokens
            user_profile.save()
            host_profile.save()
            
            return HttpResponse('Actualización de tokens exitosa')
        
        except UserProfile.DoesNotExist:
            return HttpResponse('Usuario no encontrado', status=400)
        
        except Exception as e:
            return HttpResponse('Error en la actualización de tokens', status=500)
    

"""@login_required
def room(request):
    return render(request,'base/room.html')"""
def pruebaUno(request):
    return render(request, 'base/pruebaUno.html')
def contenido(request):
    return render(request, 'base/contenido.html')
def pruebaDos(request):
    return render(request, 'base/contenidoDos.html')

class vistaInicio(View):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
        def get(self,request):
            estatus = Estatus.objects.all()
            return render(request, 'base/index.html', {'estatus': estatus})
        
        def put(self, request):     
            data = json.loads(request.body)
            channel = data.get('channel')
            estado = data.get('estado')
            Estatus.objects.filter(channel=channel).delete()
            objeto_estatus = Estatus(channel = channel, estado = estado)
            objeto_estatus.save()
        
@login_required
def profile(request):
    return render(request,'base/profile.html')
@login_required
def admin_profile(request):
    return render(request, 'base/admin_profile.html')
def exit(request):
    logout(request)
    return redirect('inicio')
"""def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_profile')
            else:
                return redirect('profile')
        else:
            return redirect('login')  
    return render(request, 'registration/login.html')
"""
def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_profile')
                else:
                    return redirect('profile')
            else:
                return redirect('login')  
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')

    return render(request, 'registration/register.html', data)
@login_required
def crudInformacion(request):
    return render(request, 'base/crud_user.html')
@login_required
def myTokens(request):
    user_profile = UserProfile.objects.get(user=request.user)
    tokens = user_profile.tokens
    return render(request,'base/misTokens.html', {'tokens':tokens})
@login_required
def myMoney(request):
    return render(request, 'base/money.html')
@login_required
def buzon(request):
    return render(request, 'base/buzon.html')
@login_required
def validacion(request):
    return render(request, 'base/validacion.html')
@login_required
def resolverDenuncia(request):
    return render(request, 'base/resolverDenuncia.html')
@login_required
def crearCategorias(request):
    return render(request, 'base/crudCategorias.html')
def tokens(request):
    paquetes = Paquetes.objects.all()
    return render(request, 'base/tokens.html', {'paquetes': paquetes})
def nosotros(request):
    return render(request, 'base/nosotros.html')
def categorias(request):
    return render(request, 'base/categorias.html')

"""class vistaTokens(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        tokens = request.POST.get('tokens')
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.tokens = tokens
        user_profile.save()
        return HttpResponse('Actualización de tokens exitosa')"""
def previo(request):
    return render(request, 'base/previo.html')

"""def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    user = User.objects.get(username__iexact=room_name)
    host_id= user.id

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'user_id' : host_id})"""

class room(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, room_name):
        espectador = UserProfile.objects.get(user=request.user)
        tokensEspectador = espectador.tokens
        username = request.GET.get('username', 'Anonymous')
        user = User.objects.get(username__iexact=room_name)
        hostId= user.id

        
            
    
        return render(request, 'base/room.html', {'room_name': room_name, 'username': username, 'user_id' : hostId, 'tokensEspectador': tokensEspectador})
    
    """def put(self, request):
        data = json.loads(request.body)
        tokens = int(data.get('tokens')) 
        tokens = data.get('tokens')
        user_profile = UserProfile.objects.get(user=request.user)
        
        host = data.get('hostId')

        user_profile.tokens += tokens
        user_profile.save()
        return HttpResponse('Actualización de tokens exitosa')

        data = json.loads(request.body)
        tokens = int(data.get('tokens'))
        host_id = data.get('hostId')
        
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            host_profile = UserProfile.objects.get(user_id=host_id)
            
            if tokens > user_profile.tokens:
                return HttpResponse('No tienes suficientes tokens', status=400)
            
            user_profile.tokens -= tokens
            host_profile.tokens += tokens
            user_profile.save()
            host_profile.save()
            
            return HttpResponse('Actualización de tokens exitosa')
        
        except UserProfile.DoesNotExist:
            return HttpResponse('Usuario no encontrado', status=400)
        
        except Exception as e:
            return HttpResponse('Error en la actualización de tokens', status=500)
    """
        
class vistaCheckout(View):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
        def get(self, request, paquete_id):
            paquete = Paquetes.objects.get(id=paquete_id)
            return render(request,'base/checkout.html', {'paquete': paquete})


class vistaExitoso(View):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
        def get(self, request, paquete_id):
            paquete = Paquetes.objects.get(id=paquete_id)
            return render(request,'base/checkoutExitoso.html', {'paquete': paquete})

        def put(self, request):
            data = json.loads(request.body)
            tokens = int(data.get('tokens')) 
            tokens = data.get('tokens')
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.tokens += tokens
            user_profile.save()
            return HttpResponse('Actualización de tokens exitosa')

class subirVideo(View):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
        def get(self, request):
            videos_del_usuario = videos.objects.filter(user=request.user)
            s3 = boto3.client('s3', 
            aws_access_key_id = 'AKIAUQIPTLA4NKIENKFW',
            aws_secret_access_key = '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')
            bucket_name = 'pruebaskills'
            nombres_videos = [video.videos for video in videos_del_usuario if video.videos]
            
            videos_base64 = []
            for nombre in nombres_videos:
                key = nombre
                response = s3.get_object(Bucket=bucket_name, Key=key)
                video_content = response['Body'].read()
                video_base64 = base64.b64encode(video_content).decode('utf-8')
                videos_base64.append(video_base64)
   
            return render(request,'base/subirVideo.html', {'videos': videos_base64})
        
        def post (self, request):

            try:
                user_profile = videos.objects.get(user=request.user)
            except ObjectDoesNotExist:
                user_profile = videos(user=request.user)

            
            uploaded_file = request.FILES['video_file'] 
            file_name = uploaded_file.name
            # Guarda el archivo subido en el bucket de S3 utilizando Boto3
            s3 = boto3.client('s3', 
            aws_access_key_id = 'AKIAUQIPTLA4NKIENKFW',
            aws_secret_access_key = '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')
            bucket_name = 'pruebaskills'
            s3.upload_fileobj(uploaded_file, bucket_name, file_name)

        
            videos.objects.create(user=request.user, videos=file_name)
                
            return redirect('profile')




