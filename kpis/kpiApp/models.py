from django.db import models
from django.forms import ModelForm

# Create your models here.

TAMANO_CHOICES = (
    ('Pequeno', 'Pe.'),
    ('Mediano', 'Md.'),
    ('Grande', 'Gr.'),
)

FUENTE_CHOICES = (
    ('Arial', 'Ar'),
    ('Verdana', 'Ve'),
)
POSICION_CHOICES = (
    ('Derecha', 'Der'),
    ('Izquierda', 'Izq'),
)


class Representante(models.Model):
	nombre = models.CharField( max_length = 100 )
	email = models.EmailField()

	def __str__(self):
		return self.nombre

	def __unicode__ (self):
		return self.nombre

class Indicador(models.Model):		
	nombre		= models.CharField( max_length = 100 )
	metrica 	= models.CharField( max_length = 100 )

	def __str__(self):
		return self.nombre

	def __unicode__ (self):
		return self.nombre

class Organizacion(models.Model):
	nombre	= models.CharField( max_length = 100 )	
	tamano = models.CharField( max_length = 20, choices=TAMANO_CHOICES)
	txt_color 	= models.CharField( max_length = 100 )
	fuente = models.CharField( max_length = 20, choices=FUENTE_CHOICES)
	logo_url	= models.CharField( max_length = 500 )
	posicion = models.CharField( max_length = 20, choices=POSICION_CHOICES)
	indicadores = models.ManyToManyField(Indicador)
	representante = models.ForeignKey(Representante)

	def __str__(self):
		return self.nombre

	class Admin:
		list_display = ('nombre', 'logo_url', 'representante', 'indicadores')



	



