from django.urls import path
from . import views
from .views import register_user, PromoMainPageView, login_user
from django.contrib.auth.views import LogoutView
from yummix.settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('', PromoMainPageView.as_view(), name='promo-main'),
    path('register/', register_user, name='register'),
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', login_user, name='login')
]
