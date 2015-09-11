from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from bassculture.views.home import HomeView
from bassculture.views.fhome import FhomeView
from bassculture.views.about import AboutView
from bassculture.views.resources import ResourcesView
from bassculture.views.source import SourceList, SourceDetail
from bassculture.views.author import AuthorList, AuthorDetail
from bassculture.views.tune import TuneList, TuneDetail
from bassculture.views.item import ItemList, ItemDetail
from bassculture.views.search import SearchView

urlpatterns = patterns('',

                       url(r'^$', HomeView.as_view(), name='home'),

                       url(r'^fiddle/$', FhomeView.as_view(), name='fhome'),

                       url(r'^fiddle/search/$', SearchView.as_view(), name="search-view"),

                       url(r'^fiddle/authors/$', AuthorList.as_view(),
                           name="author-list"),

                       url(r'^fiddle/author/(?P<pk>[a-zA-Z0-9]+)/$',
                           AuthorDetail.as_view(), name="author-detail"),

                       url(r'^fiddle/tunes/$', TuneList.as_view(), name="tune-list"),

                       url(r'^fiddle/tune/(?P<pk>[a-zA-Z0-9]+)/$',
                           TuneDetail.as_view(), name="tune-detail"),

                       url(r'^fiddle/copies/$', ItemList.as_view(), name="item-list"),

                       url(r'^fiddle/copy/(?P<pk>[a-zA-Z0-9]+)/$',
                           ItemDetail.as_view(), name="item-detail"),

                       url(r'^fiddle/sources/$', SourceList.as_view(),
                           name="source-list"),

                       url(r'^fiddle/source/(?P<pk>[a-zA-Z0-9]+)/$',
                           SourceDetail.as_view(), name="source-detail"),

                       url(r'^fiddle/about/$', AboutView.as_view(), name="about"),

                       url(r'^fiddle/resources/$', ResourcesView.as_view(), name="about"),

                       url(r'^admin/', include(admin.site.urls)),
                       )

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
