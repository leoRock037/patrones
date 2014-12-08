from django.conf.urls import patterns, include, url

#Function based API views
from api.views import org_lista

# Class based API views
#from api.views import TaskList, TaskDetail

urlpatterns = patterns('',

    #Regular URLs
	url(r'^org/$', org_lista, name='org_list'),
)