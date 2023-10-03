from django.shortcuts import render
from.models import Rescatados
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from blog.serializers import UserSerializer, GroupSerializer
# Create your views here.
def Mostrar(request):
    
    return render(request, 'Trabajo_Perrits_good.html',{})



def listarRescatados(request):
    lista= Rescatados.objects.all()
    return render(request, 'rescatados.html',{'lista':lista})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]