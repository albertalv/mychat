from django.shortcuts import render,redirect
from agora_token_builder import RtcTokenBuilder
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from .forms import LoginForm
from .forms import CustomUserCreationForm
from .models import Stream
import random
import time 
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
@login_required
def lobby(request):
    return render(request,'base/lobby.html')
@login_required
def room(request):
    return render(request,'base/room.html')
def pruebaUno(request):
    return render(request, 'base/pruebaUno.html')
def contenido(request):
    return render(request, 'base/contenido.html')
def pruebaDos(request):
    return render(request, 'base/contenidoDos.html')
def inicio(request):
    streams = Stream.objects.all()
    return render(request, 'base/index.html', {'streams': streams, 'connected': connected})
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
    return render(request,'base/misTokens.html')
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
    return render(request, 'base/tokens.html')
def nosotros(request):
    return render(request, 'base/nosotros.html')
def categorias(request):
    return render(request, 'base/categorias.html')

