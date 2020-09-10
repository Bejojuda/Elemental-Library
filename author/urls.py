from django.urls import path
from django.conf.urls import url
from .views import AuthorView, AuthorDetailsView

urlpatterns = [
    path('', AuthorView.as_view()),
    path('<int:pk>/', AuthorDetailsView.as_view()),

    url('^(?P<parmas>.+)/$', AuthorView.as_view()),
]