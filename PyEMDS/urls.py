from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from EMDSapp.views import group_remove

urlpatterns = patterns('',
    url(r'^$', 'EMDSapp.views.main_page'),

    url(r'^specialty/add/$', 'EMDSapp.views.specialty_add'),
    url(r'^specialty/remove/(\d+)$', 'EMDSapp.views.specialty_remove'),
    url(r'^specialty/edit/(\d+)/$', 'EMDSapp.views.specialty_edit'),
    url(r'^specialty/$', 'EMDSapp.views.specialty_list'),

    url(r'^group/add$', 'EMDSapp.views.group_add'),
    url(r'^group/remove/(\d+)$', 'EMDSapp.views.group_remove'),
    url(r'^group/edit/(\d+)$', 'EMDSapp.views.group_edit'),
    url(r'^group/$', 'EMDSapp.views.group_list'),


    # Examples:
    # url(r'^$', 'PyEMDS.views.home', name='home'),
    # url(r'^PyEMDS/', include('PyEMDS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# handler404 = 'mysite.views.my_custom_404_view'