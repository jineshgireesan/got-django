from django.contrib import admin
from django.urls import path, include
from accounts.views import create_admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', create_admin),
    path('', include('accounts.urls')),
]

# This line makes images work in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)