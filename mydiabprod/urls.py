
from django.urls import path
from django.conf.urls import url
from . import views
#from django.conf import settings
## from django.conf.urls.static import static


app_name = 'mydiabprod'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('<str:question>/', views.detail, name='detail'),
    #path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    #path(r'^$', views.upload_file, name='upload_file'),
    path('specific/', views.specific, name='specific'),
    path('login/', views.login, name='login'),
    path('loginx/', views.loginx, name='loginx'),
    path('ajax/', views.ajax, name='ajax'),
    path('logout/', views.logout, name='logout'),
    #
    path('upload_file/', views.upload_file, name='upload_file'),
    path('charts/', views.charts, name='charts'),
    #path('texarea/', views.textarea, name='textarea'),
    #path('media/', views.upload_file, name=''),
    path('calendarium/', views.calendarium, name='calendarium'),
    path('eventlogx/', views.eventlogx, name='eventlogx'),
    path('richtextblog/', views.richtextblog, name='richtextblog'),
    path('calendar/', views.calendarx, name='calendarx'),
    path('delevent/', views.delevent, name='delevent'),
    path('calendarmainlist/', views.calendarmainlist, name='calendarmainlist'),
    path('checkevent/', views.checkevent, name='checkevent'),
    path('checkeventsecond/', views.checkeventsecond, name='checkeventsecond'),
    path('eventum/', views.eventum, name='eventum'),
    path('currentweek/', views.currentweek, name='currentweek'),
    path('quotidie/', views.quotidie, name='quotidie'),
    #path('pers/', views.pers, name='pers'),
    path('instantimage/', views.instantimage, name='instantimage'),
	path('instantimageremove/', views.instantimageremove, name='instantimageremove'),
	path('pers_blog/', views.pers_blog, name='pers_blog'),
	path('blog_counter/', views.blog_counter, name='blog_counter'),
	path('postremove/', views.postremove, name='postremove'),
	path('postsetpublic/', views.postsetpublic, name='postsetpublic'),
	path('postsetprivate/', views.postsetprivate, name='postsetprivate'),
	path('getforwards/', views.getforwards, name='getforwards'),
	path('getpostx/', views.getpostx, name='getpostx'),
	path('searchblogx/', views.searchblogx, name='searchblogx'),
	path('getsearch/', views.getsearch, name='getsearch'),
    path('getpostdisplay/', views.getpostdisplay, name='getpostdisplay'),
	path('updatepost/', views.updatepost, name='updatepost'),
	path('getpostdisplaynext/', views.getpostdisplaynext, name='getpostdisplaynext'),
    path('registerx/', views.registerx, name='registerx'),
    path('checkun/', views.checkun, name='checkun'),
    path('registerun/', views.registerun, name='registerun')
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
