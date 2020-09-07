from django.urls import path

from .views import BookView, BookDetailView, BookUnitView

urlpatterns = [
    path('', BookView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('unit/', BookUnitView.as_view())
]