from django.conf.urls import url
from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.employeeview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
