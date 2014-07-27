from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView


from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    (r'^accounts/', include('allauth.urls')),
    url(r'^tracker/', include('tracker.urls', namespace='tracker', app_name='tracker')),


)


#urlpatterns += patterns('django.contrib.auth.views',
#
#    url(r'^login/$', 'login', {'template_name': 'users/login.html',}, name='login'),
#    url(r'^logout/$', 'logout', {'template_name': 'users/login.html'},name='logout'),
#
#
#)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
