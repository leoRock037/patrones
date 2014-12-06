from django.db import models

# Create your models here.
class Organizacion(models.Model):
	nombre	= models.CharField( max_length = 100 )
	logo	= models.CharField( max_length = 100 )
	color 	= models.CharField( max_length = 100 )


class Kpi(models.Model):
	responsable = models.CharField( max_length = 100 )
	tipo 		= models.CharField( max_length = 100 )
	metrica 	= models.CharField( max_length = 100 )
	organizacion = models.ManyToManyField(Organizacion)

