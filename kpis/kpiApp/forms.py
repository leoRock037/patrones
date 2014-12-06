from django import forms

from models import Organizacion

class addKpiForm(forms.Form):
	responsable		= forms.CharField(widget=forms.TextInput())
	tipo			= forms.CharField(widget=forms.TextInput())
	metrica			= forms.CharField(widget=forms.TextInput())
	organizacion	= forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all())

	def clean(self):
		return self.cleaned_data
