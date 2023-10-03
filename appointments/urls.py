from django.urls import path
from .views import list_doctors,doctor_detail,book_appointment

urlpatterns = [
    path('doctors/', list_doctors, name='list_doctors'),
    path('doctors/<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('book-appointment/', book_appointment, name='book_appointment'),
]