from .models import RestaurantInfo


#Контекстные процессоры позволяют сделать данные доступными во всех шаблонах без явного указания в каждом представлении.
def restaurant_context(request):
    if request.user.is_authenticated:
        try:
            restaurant = RestaurantInfo.objects.get(restaurant_owner=request.user)
            return {'restaurant': restaurant}
        except RestaurantInfo.DoesNotExist:
            return {}
    return {}
