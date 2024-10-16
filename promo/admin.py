from django.contrib import admin
from .models import Currency, RestaurantInfo, DishCategory, DishItem, BarCategory, BarItem

admin.site.register(Currency)
admin.site.register(RestaurantInfo)
admin.site.register(DishCategory)
admin.site.register(DishItem)
admin.site.register(BarCategory)
admin.site.register(BarItem)

