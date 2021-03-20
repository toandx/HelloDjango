from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from db.models import KeyWord,User,Data
from db.serializers import KeyWordSerializer, UserSerializer, DataSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import os.path

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
STATIC_PATH=os.path.join(PROJECT_PATH,'static')
MEDIA_PATH=os.path.join(STATIC_PATH,'media')
print(MEDIA_PATH)

@csrf_exempt
def keyword_list(request):
    """
    List all code keyword, or create a new snippet.
    """
    if request.method == 'GET':
        keyword = KeyWord.objects.all()
        serializer = KeyWordSerializer(keyword, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KeyWordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400) 

@csrf_exempt
def keyword_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = KeyWord.objects.get(pk=pk)
    except KeyWord.DoesNotExist:
        return HttpResponse(status=404)
 
    if request.method == 'GET':
        serializer = KeyWordSerializer(snippet)
        return JsonResponse(serializer.data)
 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = KeyWordSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
 
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@api_view(['POST'])
def keyword_add(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        key=KeyWord(name=data['name'],des=data['des'])
        key.save()
        content = {'status': 1}
        return JsonResponse(content, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_list(request):
    """
    List all code keyword, or create a new snippet.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_login(request):
    """
    List all code keyword, or create a new snippet.
    """
    if True:
        data = JSONParser().parse(request)
        usr_name=data['usr_name']
        try:
            snippet = User.objects.get(usr_name=usr_name)
        except User.DoesNotExist:
            return HttpResponse(status=404)
        serializer = UserSerializer(snippet)
        return HttpResponse(status=200)
		
@api_view(['GET'])
def custom(request, format=None):
    content = {'user_count': 1}
    return JsonResponse(content)
	
@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
 
@csrf_exempt
def data_list(request):
    """
    List all code keyword, or create a new snippet.
    """
    if request.method == 'GET':
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        myfile = request.FILES['file']
        des = request.POST['des']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        data=Data(name=myfile.name,des=request.POST['des'])
        data.save()
        serializer = DataSerializer(data)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            data = Data.objects.get(id=data['id'])
        except Data.DoesNotExist:
            return HttpResponse(status=404)       
        data.delete()
        return HttpResponse(status=204) 
    return HttpResponse(status=404)
 
@csrf_exempt
def data_download(request,name):
    file_path=os.path.join(MEDIA_PATH,name)
    print(file_path)
    file = open(file_path, 'rb')
    return FileResponse(file)
        
 
@csrf_exempt
def uploader(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        des=request.POST['des']
        fs=FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        return HttpResponse("Upload succesful")
    return HttpResponse("Upload fail") 