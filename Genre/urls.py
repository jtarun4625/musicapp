from django.conf.urls import url,include
from django.contrib import admin
from Genre import views as genre_view
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', genre_view.GenreList_View, name='GenreListView'),
    url(r'^create/', genre_view.CreateGenre_View, name='CreateGenretView'),
    url(r'^update/(?P<id>\d+)/$', genre_view.UpdateGenre_View, name='UpdateGenretView'),
    url(r'^apidata$', genre_view.datalist.as_view(), name='DataView'),
    url(r'^apidata/(?P<pk>\d+)/$', genre_view.detailAPIview.as_view(), name='DataViewAPI'),
    url(r'^apiupdate/(?P<pk>\d+)/$', genre_view.updatelist.as_view(), name='UpdateAPI'),
    url(r'^createapi/$', genre_view.createapiview.as_view(), name='createAPI'),
]
urlpatterns = format_suffix_patterns(urlpatterns)