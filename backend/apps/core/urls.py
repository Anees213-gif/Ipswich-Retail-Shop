from django.urls import path
from . import views
from .health import health

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('health/', health, name='health-check'),
    path('metrics/', views.metrics, name='metrics'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
]
