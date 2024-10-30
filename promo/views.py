from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from .forms import CustomUserCreationForm
from django.contrib import messages
from restaurant_admin.models import RestaurantInfo
from django.contrib.auth import logout, authenticate, login
from .forms import LoginUserForm


class PromoMainPageView(ListView):
    template_name = 'promo/promo-main.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return RestaurantInfo.objects.all()


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-main')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'promo/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('admin-main'))
    else:
        form = LoginUserForm()
    form = LoginUserForm
    return render(request, 'promo/login.html', {'form': form})
