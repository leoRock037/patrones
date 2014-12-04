from django import forms


class addKpiForm(forms.Form):
	responsable		= forms.CharField(widget=forms.TextInput())
	tipo			= forms.CharField(widget=forms.TextInput())
	metrica			= forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
