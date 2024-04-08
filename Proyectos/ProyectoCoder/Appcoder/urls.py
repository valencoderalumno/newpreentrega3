from django.urls import path
from Appcoder.views import * 

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('cursos/', Curso, name="Cursito"),
    path('profesores/', profesor, name="Profesores"),
    path('entregables/', entregable, name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path("cursoformu/", CursoFormulario, name="formulariocurso"),
    path("leerprofesores/", leerprofesores, name="ProfesLeer" ),
    path("Crearprofes/", Crearprofesores, name="ProfesCrear" ),
    path("eliminarprofes/<profeNombre>", eliminarprofesores, name="eliminarprofesores" )

]



