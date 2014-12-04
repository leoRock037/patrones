from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from forms import addKpiForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Kpi


def addKpi_view(request):
	info = "Inicializando" 
	if request.method == "POST":
		form = addKpiForm(request.POST)
		if form.is_valid():
			responsable = form.cleaned_data['responsable']
			tipo = form.cleaned_data['tipo']
			metrica = form.cleaned_data['metrica']
			organizacion = form.cleaned_data['organizacion']
			k = Kpi()
			k.responsable 		=  responsable
			k.tipo 	= tipo
			k.metrica 		= metrica
			k.status = True
			k.save() # Guardar la informacion
			info = "Se guardo satisfactoriamente!!!!!"
		else:
			info = "informacion con datos incorrectos"			
	form = addKpiForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('addKpi.html',ctx,context_instance=RequestContext(request))
