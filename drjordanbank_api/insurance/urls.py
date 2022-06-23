from django.urls import path
from . import views

urlpatterns = [
    path('api/insurance', views.InsuranceList.as_view(), name='insurance_list'),
    path('api/insurance/<int:pk>', views.InsuranceDetail.as_view(), name='insurance_detail'),
]
