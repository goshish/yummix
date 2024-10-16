from django.urls import path
from . import views
from .views import AdminMain


urlpatterns = [
    path('', AdminMain.as_view(), name='admin-main'),
]