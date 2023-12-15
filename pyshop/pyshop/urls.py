
from django.contrib import admin
from django.urls import path, include



from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
    #path('products/new/', include('products.urls')),

    path('core/', include('core.urls')),
    #path('contact/', contact, name='contact'),

    path('items/',include('item.urls')),

    path('dashboard/', include('dashboard.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
