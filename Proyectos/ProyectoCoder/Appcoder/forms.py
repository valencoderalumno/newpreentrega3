from django import forms
from Appcoder.models import*


class cursoformu(forms.Form):
  
    curso = forms.CharField()
    camada = forms.IntegerField()



class Profeformu(forms.Form):
  nombre = forms.CharField(max_length=60)
  apellido = forms.CharField(max_length=60)
  correo = forms.EmailField()
  profesion = forms.CharField(max_length=60) 