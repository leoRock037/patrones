from django.conf.urls import patterns, include, url

# Function based API views
from api.views import kpi_lista

# Class based API views
#from api.views import TaskList, TaskDetail

urlpatterns = patterns('',

    #Regular URLs
	url(r'^kpi/$', kpi_lista, name='kpi_list'),
)