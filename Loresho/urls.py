from django.contrib import admin
from django.urls import path, include
from Loresho.backend.admin import loresho_site
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', loresho_site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
