from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('promo.urls')),
    path('restaurant_admin/', include('restaurant_admin.urls'), name="admin-main"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)