from django.urls import path
from . import views

urlpatterns = [
    path('api/appointments', views.AppointmentList.as_view(), name='appointment_list'),
    path('api/appointments/<int:pk>', views.AppointmentDetail.as_view(), name='appointment_detail'),
]
