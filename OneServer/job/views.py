from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from db.models import KeyWord,User
from db.serializers import KeyWordSerializer, UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

@api_view(['GET'])
def homepage(request):
    return render(request, 'home.html')
    
@api_view(['GET'])
def dictpage(request):
    return render(request, 'dict.html')

@api_view(['GET'])
def datapage(request):
    return render(request, 'data.html')