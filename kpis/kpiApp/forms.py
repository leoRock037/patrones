from django import forms

from models import *


# class KpiForm(forms.Form):
# 	responsable		= forms.CharField(widget=forms.TextInput())
# 	tipo			= forms.CharField(widget=forms.TextInput())
# 	metrica			= forms.CharField(widget=forms.TextInput())	

# class addKpiForm(forms.ModelForm):
# 	class Meta:
# 		model = Kpi
# 		exclude = {'status', }

# class OrganizacionForm(forms.Form):
# 	nombre	= forms.CharField(widget=forms.TextInput())
# 	logo	= forms.CharField(widget=forms.TextInput())
# 	color 	= forms.CharField(widget=forms.TextInput())

# class addOrganizacionForm(forms.ModelForm):
# 	class Meta:
# 		model = Organizacion
# 		exclude = {'status', }