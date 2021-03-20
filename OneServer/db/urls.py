from django.urls import path
from db import views

urlpatterns = [
    path('keyword/', views.keyword_list),
    path('keyword/<int:pk>/', views.keyword_detail),
    path('user/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
    path('data/', views.data_list),
    path('download/<str:name>/', views.data_download),
    path('custom/', views.custom),
]