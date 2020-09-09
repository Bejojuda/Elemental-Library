from django.urls import path

from .views import RentalView, RentalBorrowView, RentalReturnView, RentalDetailsView

urlpatterns = [
    path('', RentalView.as_view()),
    path('borrow/', RentalBorrowView.as_view()),
    path('return/<int:pk>/', RentalReturnView.as_view()),
    path('<int:pk>/', RentalDetailsView.as_view()),
]