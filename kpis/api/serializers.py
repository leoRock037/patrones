from rest_framework import serializers
from kpiApp.models import Kpi

class KpiSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Kpi
		fields = ('id','responsable','tipo','metrica','organizacion' )