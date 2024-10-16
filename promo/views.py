from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import RestaurantInfo, User


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
            messages.success(request, "Registration successful.")
            return redirect('promo-main ')  # Редирект после успешной регистрации
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'promo/register.html', context)

