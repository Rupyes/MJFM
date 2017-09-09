from django.conf.urls import url
from . import views


app_name = 'fm_app'

urlpatterns = [
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.ContactFormView.as_view(), name='contact'),
    url(r'^listofnews/$', views.NewsListView.as_view(), name='listofnews'),
    url(r'^listsofnews/(?P<pk>\d+)$', views.NewsDetailView.as_view(), name='news_details'),
    url(r'^one_news/(?P<newstype>[-\w]+)$', views.OneCategoryView.as_view(), name='one_category_news'),
    url(r'^thanks/$', views.Thanks.as_view(), name='thanks'),
    url(r'^program_schedule/$', views.ProgramSchedule.as_view(), name='schedule'),
    url(r'^profiles/$', views.ProfileView.as_view(), name='profiles'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
]
