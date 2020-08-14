from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from .models import profile

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import profile
from .serializers import profileSerializer
# Create your views here.
class profileList(APIView):
      def get(self,request):
          profiles=profile.objects.all()
          serializer=profileSerializer(profiles,many=True)
          return Response(serializer.data)

      def post(self):
         pass     



def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method=='GET':
     
      user=request.GET['username']
      try:
          User.objects.get(username=user)
          return render(request,'signup.html',{'msg':'Username is already exists'})
      except User.DoesNotExist:

          if request.GET['password']==request.GET['repassword']:
              User.objects.create_user(username=request.GET['username'],password=request.GET['password'])
              return render(request,'signup.html',{'msg':'sucessfully register'})
            
          else:
              return render(request,'signup.html',{'msg':'Password Incorrect'})
    else:
        return render(request,'signup.html')  

def signin(request):
    return render(request,'about.html')     

def login(request):
    if request.method=='GET':
        user=auth.authenticate(username=request.GET['username'],password=request.GET['password'])
        if user is not None:
            auth.login(request,user)
      
            return redirect(home)        
        else:
            return render(request,'about.html',{'error':'invalid login credential'})
    else:
        return render(request,'about.html')       


def student(request):
    if request.method=='POST' and request.FILES['myfile']:
  
        myfiles=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfiles.name, myfiles)
        url=fs.url(filename)
        new_profile=profile(            
            studentname=request.POST['studentname'],
            studentemail=request.POST['studentemail'],
            studentphone=request.POST['studentphone'],
            studentage=request.POST['studentage'],
            studentrollno=request.POST['studentrollno'],
            studentgender=request.POST['studentgender'],
            image=url,
            user=request.user,
        )
        new_profile.save()
        return render(request,'student.html')   
        
    else:
        return render(request,'student.html')        

def home(request):
    loguser=request.user
    all_uploads=profile.objects.filter(user=loguser)#ya tira confusion cha
    return render(request,'add.html',{'uploads':all_uploads})

def logout(request):
    auth.logout(request)
    return redirect(signin)

def addstu(request):
    if request.method=='POST':
        return render(request,'student.html')
    else:
        return render(request,'add.html')    

def delete(request,todo_id):
    item=profile.objects.get(id=todo_id)
    item.delete()
    return redirect(home)

 