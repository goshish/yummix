from django.views.generic import ListView
from .models import RestaurantInfo


class AdminMainPageView(ListView):
    template_name = 'restaurant_admin/admin-main.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return RestaurantInfo.objects.all()
