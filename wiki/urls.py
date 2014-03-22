from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sistema.views',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', RedirectView.as_view(url='/wiki/index/')),
    (r'^wiki/(?P<nomePagina>[^/]+)/$', 'mostrar_pagina'),
    (r'^wiki/(?P<nomePagina>[^/]+)/editar/$', 'editar_pagina'),
    (r'^wiki/(?P<nomePagina>[^/]+)/salvar/$', 'salvar_pagina'),
)
