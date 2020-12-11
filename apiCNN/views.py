from django.shortcuts import render

from rest_framework import generics
from apiCNN import models
from apiCNN import forms
from apiCNN import serializers

from django.shortcuts import render, redirect 
from django.http import HttpResponse 
import pyrebase
from apiCNN.Logic import modelCNN
# Create your views here.
config = {

    'apiKey': "AIzaSyDBYpL2tb3yh3SIPo2BFhlS7slKruVGOic",
    'authDomain': "proyectotiendajpri.firebaseapp.com",
    'databaseURL': "https://proyectotiendajpri.firebaseio.com",
    'projectId': "proyectotiendajpri",
    'storageBucket': "proyectotiendajpri.appspot.com",
    'messagingSenderId': "1046831721926",
    'appId': "1:1046831721926:web:7402a636a8cd165f4b16c7",
    'measurementId': "G-MKSCN84RDE"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class Autenticacion():

    def singIn(request):

        return render(request, "signIn.html")

    def postsign(request):
        email=request.POST.get('email')
        passw = request.POST.get("pass")
        try:
            user = auth.sign_in_with_email_and_password(email, passw)
        except:
            message = "invalid cerediantials"
            return render(request,"signIn.html",{"msg":message})
        print(user)
        return render(request, "welcome.html",{"e":email})

class UploadImage():
    def image_view(request):
        if request.method == 'POST': 
            form = forms.ImageForm(request.POST, request.FILES)
            if form.is_valid():
                
                img = form.save(commit=False)
                img.save()
                path = img.image.url
                certainty, prediction_result = modelCNN.modelCNN.predictScene(modelCNN.modelCNN, path)
                return render(request, "results.html", {"result": prediction_result,  "certainty": certainty, "path": img.image.url[1:]})
        else: 
            form = models.UploadImage()
        return render(request, 'scene.html', {'form' : form}) 
  
  
    def success(request):
        path = request.POST.get('image')
        print( path)
        predictScene(request)
        # return "render(request, 'scene_predict', {'path' : path})"

class Classification():
    def determineScene(request):
        return render(request, "scene.html")

    def predictScene(request):
        try:
            path = request.GET.get('path')
            print("\n\nPATH: ", path, "\n\n")
            if(path == 'default'):
                path = 'D:/documents/u/ciclo_7/aprendizaje_maquina/practicas/5.ActividadRecursosRedesNeuronalesAvanzadasImagenes/ProyectoMLbase/1.ProyectoMLbase/apiCNN/templates/img/5.jpg'
            
        except:
            path = 'D:/documents/u/ciclo_7/aprendizaje_maquina/practicas/5.ActividadRecursosRedesNeuronalesAvanzadasImagenes/ProyectoMLbase/1.ProyectoMLbase/apiCNN/templates/img/5.jpg'
        
        result = modeloSNN.modeloSNN.predictScene(modeloSNN.modeloSNN, path)
        return render(request, "welcome.html", {"result": result, "path": path})

# https://www.geeksforgeeks.org/python-uploading-images-in-django/