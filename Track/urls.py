from django.conf.urls import url,include
from django.contrib import admin
from Track import views as track_view
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', track_view.List_View, name='ListView'),
    url(r'^createtrack/$', track_view.Create_track , name='createtrack'),
    url(r'^edit/(?P<id>\d+)/$', track_view.Update_track , name='updatetrack'),
    url(r'^delete/(?P<id>\d+)/$', track_view.Delete_track , name='deletetrack'),
    url(r'^details/(?P<id>\d+)/$', track_view.Track_detail,name='Trackdetail'),
    url('^search/(?P<username>.+)/$', track_view.SearchList.as_view()),
    url(r'^apidata$', track_view.datalist.as_view(), name='DataView'),
    url(r'^apidata/(?P<pk>\d+)/$', track_view.detailAPIview.as_view(), name='DataViewAPI'),
    url(r'^apiupdate/(?P<pk>\d+)/$', track_view.updatelist.as_view(), name='UpdateAPI'),
    url(r'^createapi/$', track_view.createapiview.as_view(), name='createAPI'),
]

urlpatterns = format_suffix_patterns(urlpatterns)