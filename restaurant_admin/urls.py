from django.urls import path
from . import views
from .views import AdminMainPageView, DishCategoryDetailView, BarCategoryView, BarCategoryDetailView, RestaurantInfoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-main/', AdminMainPageView.as_view(), name='admin-main'),
    path('dish-category/<slug:slug>/', DishCategoryDetailView.as_view(), name='dish-category-detail'),
    path('bar-categories', BarCategoryView.as_view(), name='bar-categories'),
    path('bar-category/<slug:slug>/', BarCategoryDetailView.as_view(), name='bar-category-detail'),
    path('restaurant-info/', RestaurantInfoView.as_view(), name='restaurant-info'),
]
