from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import Home


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kpis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url( r'^$', Home.as_view() ),

    url(r'^admin/', include(admin.site.urls)),
	url( r'^api/', include( 'api.urls' ) ),
	url( r'^kpi/', include( 'kpiApp.urls' ) ),
)