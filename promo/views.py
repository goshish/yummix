from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import CustomUserCreationForm
from django.contrib import messages
from restaurant_admin.models import RestaurantInfo


class PromoMainPageView(ListView):
    template_name = 'promo/promo-main.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return RestaurantInfo.objects.all()


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promo-main')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'promo/register.html', context)
