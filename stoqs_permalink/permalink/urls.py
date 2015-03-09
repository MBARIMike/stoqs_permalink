# permalink/urls.py
from django.conf.urls import patterns, url

from permalink import views

urlpatterns = patterns('',
    url(
        regex = '^api/$',
        view = views.PermalinkCreateView.as_view(),
        name = 'permalink_rest_api'
    ),
##    url(
##        regex = '^api/(?P<slug>[-\w]+)/$',
##        view = views.PermalinkUpdateCreateView.as_view(),
##        name = 'permalink_rest_api'
##    )
)
