from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *


# def addKpi_view(request):
# 	info = "Inicializando" 
# 	if request.method == "POST":
# 		form = addKpiForm(request.POST)
# 		if form.is_valid():
# 			add = form.save(commit=False) 
# 			add.status = True
# 			add.save() #Guarda la informacion
# 			form.save_m2m() # guarda las relaciones de ManyToMany
# 			info = "Se guardo el KPI satisfactoriamente!"
# 		else: 
# 			info = "informacion con datos incorrectos"
# 	else:		
# 		form = addKpiForm()
# 	ctx = {'form':form, 'informacion':info}
# 	return render_to_response('addKpi.html',ctx,context_instance=RequestContext(request))


# def addOrganizacion_view(request):
# 	info = "Inicializando" 
# 	if request.method == "POST":
# 		form = addOrganizacionForm(request.POST)
# 		if form.is_valid():
# 			add = form.save(commit=False) 
# 			add.status = True
# 			add.save() #Guarda la informacion			
# 			info = "Se guardo la organizacion satisfactoriamente!"
# 			#return HttpResponseRedirect('/indicador/nuevo_tipo/')
# 	else:
# 		form = addOrganizacionForm()
# 	ctx = {'form':form, 'informacion':info}
# 	return render_to_response('addOrg.html',ctx,context_instance=RequestContext(request))

# def about(request):
# 	texto = "Proyecto de Indicadores (KPIs) -  Sergio Alexander Gutierrez - CodeTag"
# 	return render (request, 'about.html', {'texto': texto})

def generador (request):
	return render (request, 'generador.html')

def generarOrg_view (request, id_org):
	i = id_org
	return render (request, 'generador.html', {'org':i})

def org_views(request):
	lorg=Organizacion.objects.all()
	ctx={'lista_org':lorg}
	return render_to_response('lista_org.html', ctx, context_instance=RequestContext(request))