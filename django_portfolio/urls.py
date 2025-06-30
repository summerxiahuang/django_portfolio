from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media'  # This matches the Render disk mount path
# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Always serve media files (safe with Render Disk)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)