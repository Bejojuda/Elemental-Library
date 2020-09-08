from django.urls import path
from .views import AuthorView, AuthorDetailsView

urlpatterns = [
    path('', AuthorView.as_view()),
    path('<int:pk>/', AuthorDetailsView.as_view())
]