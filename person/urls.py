from django.urls import path
from django.conf.urls import url

from .views import PersonView, PersonDetailsView

urlpatterns = [
    path('', PersonView.as_view(), name='people-list'),
    path('<int:pk>/', PersonDetailsView.as_view(), name='person-details'),

    url('^(?P<parmas>.+)/$', PersonView.as_view()),
]