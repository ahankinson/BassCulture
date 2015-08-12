from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from bassculture.views.home import HomeView
from bassculture.views.source import SourceList, SourceDetail
from bassculture.views.author import AuthorList, AuthorDetail
from bassculture.views.tune import TuneList, TuneDetail
from bassculture.views.item import ItemList, ItemDetail
from bassculture.views.search import SearchView

urlpatterns = patterns('',

                       url(r'^$', HomeView.as_view(), name='home'),

                       url(r'^search/$', SearchView.as_view(), name="search"),

                       url(r'^authors/$', AuthorList.as_view(),
                           name="author-list"),

                       url(r'^author/(?P<pk>[a-zA-Z0-9]+)/$',
                           AuthorDetail.as_view(), name="author-detail"),

                       url(r'^tunes/$', TuneList.as_view(), name="tune-list"),

                       url(r'^tune/(?P<pk>[a-zA-Z0-9]+)/$',
                           TuneDetail.as_view(), name="tune-detail"),

                       url(r'^items/$', ItemList.as_view(), name="item-list"),

                       url(r'^item/(?P<pk>[a-zA-Z0-9]+)/$',
                           ItemDetail.as_view(), name="item-detail"),

                       url(r'^sources/$', SourceList.as_view(),
                           name="source-list"),

                       url(r'^source/(?P<pk>[a-zA-Z0-9]+)/$',
                           SourceDetail.as_view(), name="source-detail"),

                       url(r'^admin/', include(admin.site.urls)),
                       )

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
