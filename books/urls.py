from django.conf.urls import url
from django.urls import path

from .views import BookView, BookDetailView, BookUnitView, BookUnitDetailView

urlpatterns = [
    path('', BookView.as_view()),
    path('units/', BookUnitView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('<int:book_id>/<int:pk>/', BookUnitDetailView.as_view()),

    # If placed above 'units/', that endpoint would not work
    url('^(?P<parmas>.+)/$', BookView.as_view()),
]