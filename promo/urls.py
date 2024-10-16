from django.urls import path
from . import views
from .views import register, PromoMainPageView

urlpatterns = [
    path('', PromoMainPageView.as_view(), name='promo-main'),
    path('register', register, name='register')
]
