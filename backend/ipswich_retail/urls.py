"""
URL configuration for ipswich_retail project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

def home_view(request):
    """Main page view for the root URL"""
    return JsonResponse({
        'message': 'Welcome to Ipswich Retail API',
        'version': '1.0.0',
        'status': 'healthy',
        'endpoints': {
            'api_root': '/api/',
            'categories': '/api/categories/',
            'products': '/api/products/',
            'orders': '/api/orders/',
            'customers': '/api/customers/',
            'admin': '/admin/',
            'api_docs': '/api/docs/',
            'health_check': '/api/health/',
        }
    })

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/customers/', include('apps.customers.urls')),
    
    # Admin API endpoints
    path('api/admin/', include('apps.core.admin_urls')),
    path('api/admin/products/', include('apps.products.admin_urls')),
    path('api/admin/orders/', include('apps.orders.admin_urls')),
    path('api/admin/customers/', include('apps.customers.admin_urls')),
    path('api/admin/auth/', include('apps.authentication.urls')),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
