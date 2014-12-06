from django.conf.urls import patterns, include, url

# Function based API views
from api.views import kpi_lista

# Class based API views
#from api.views import TaskList, TaskDetail

urlpatterns = patterns('',

    #Regular URLs
	url(r'^$','kpiApp.views.addKpi_view',name = 'view_addKpi'),
	url(r'^about/$','kpiApp.views.about',name = 'about'),
)