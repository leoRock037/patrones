from rest_framework import serializers
from kpiApp.models import Organizacion

class OrgSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Organizacion
		fields = ( 'nombre', 'tamano', 'txt_color', 'logo_url', 'posicion', 'indicadores', 'representante')