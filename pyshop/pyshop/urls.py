from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('core/', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include(('myroot.urls', 'myroot'), namespace='myroot')),
]

# Serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serving static files during development
# Note: You don't typically need to set STATIC_ROOT for development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
