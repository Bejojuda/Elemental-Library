from django.urls import path

from .views import BookView, BookDetailView, BookUnitDetailView

urlpatterns = [
    path('', BookView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('<int:book_id>/<int:pk>', BookUnitDetailView.as_view()),
]