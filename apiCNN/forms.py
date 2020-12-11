# forms.py 
from django import forms 
from apiCNN.models import UploadImage
  
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = UploadImage
        fields = ['image']