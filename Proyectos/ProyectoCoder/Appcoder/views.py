from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso, Profesor
from Appcoder.forms import cursoformu, Profeformu
# Create your views here.


def inicio(request):
  return render(request,"Appcoder/inicio.html")

def Curso(request):

 cur1 = Curso(nombre="Python", camada=43125)
 cur1.save

 return HttpResponse(f"El curso que he creado es: {cur1.nombre} y su camada es: {cur1.camada}")

def estudiantes(request):
  return  render(request,"Appcoder/estudiantes.html")

def profesor(request):
  return render(request,"Appcoder/profesores.html")

def entregable(request):
  return render(request,"Appcoder/entregables.html")

def CursoFormulario(request):

 if request.method == "POST":
   
   
   formulario1 = cursoformu(request.POST)
   

   if formulario1.is_valid():
       
          info = formulario1.cleaned_data

          curso = Curso(nombre=info["curso"], camada=info["camada"])
 
          curso.save()
  
          return render(request, "/Appcoder/inicio.html") 

 else:

     formulario1 = cursoformu()
 
 return render(request, "Appcoder/cursoformulario.html", {"form1": formulario1})





def leerprofesores(request):
 
   profesor = profesor.object.all()

   contexto = {"teachers": profesor}

   return render(request, "Appcoder/leerprofes.html", contexto) 






def Crearprofesores(request):
  if request.method == "POST":
   
   formulario2 = Profeformu(request.POST)

   if formulario2.is_valid():
       
       info = formulario2.cleaned_data

       profesor = Profeformu(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])
 
       profesor.save()
  
       return render(request, "/Appcoder/inicio.html") 

   else:

     formulario2 = Profeformu()
 
  return render(request, "Appcoder/profeformulario.html", {"form2": formulario2})


def eliminarprofesores (request, profeNombre):
   profesor = Profesor.objects.get(nombre=profeNombre)
   profesor.delete()

   profesores = Profesor.objects.all()
   contexto = {"teachers": profesores}

   return render(request, "Appcoder/leerprofes.html", contexto)
