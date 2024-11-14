from django.urls import path
from . import views
from .views import AdminMainPageView, DishCategoryDetailView, BarCategoryView, BarCategoryDetailView


urlpatterns = [
    path('admin-main/', AdminMainPageView.as_view(), name='admin-main'),
    path('dish-category/<slug:slug>/', DishCategoryDetailView.as_view(), name='dish-category-detail'),
    path('bar-categories', BarCategoryView.as_view(), name='bar-categories'),
    path('bar-category/<slug:slug>/', BarCategoryDetailView.as_view(), name='bar-category-detail')
]