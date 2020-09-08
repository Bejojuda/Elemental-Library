from django.urls import path

from .views import RentalView, RentalDetailsView

urlpatterns = [
    path('', RentalView.as_view()),
    path('<int:pk>/', RentalDetailsView.as_view()),
]