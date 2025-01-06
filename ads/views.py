from django.shortcuts import render, get_object_or_404
from .models import Listing, Category
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
from django.db.models import Q

# Представлення для сторінки "Ласкаво просимо"
def welcome(request):
    return render(request, 'auth/welcome.html')

@login_required
# Представлення для відображення списку всіх оголошень
def listing_list(request):
    # Базовий queryset
    listings = Listing.objects.all()
    categories = Category.objects.all()

    # Пошук
    search_query = request.GET.get('search', '')
    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Фільтрація за категорією
    selected_category = request.GET.get('category', None)  # Отримуємо ID вибраної категорії
    if selected_category:
        listings = listings.filter(category_id=selected_category)

    context = {
    'listings': listings,
    'categories': categories,
    'selected_category': selected_category,
    }
    return render(request, 'ads/listing_list.html', context)

@login_required
# Представлення для перегляду одного оголошення
def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)  # Отримуємо оголошення за його id (pk)
    return render(request, 'ads/listing_detail.html', {'listing': listing})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} було успішно створено! Ви можете увійти.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'ads/dashboard.html')

@login_required
def my_listings(request):
    user_listings = Listing.objects.filter(owner=request.user)  # Фільтруємо оголошення за поточним користувачем
    return render(request, 'ads/my_listings.html', {'listings': user_listings})

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('my_listings')
    else:
        form = ListingForm()
    return render(request, 'ads/create_listing.html', {'form': form})

@login_required
def edit_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('my_listings')
    else:
        form = ListingForm(instance=listing)
    return render(request, 'ads/edit_listing.html', {'form': form})

@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == 'POST':
        listing.delete()
        return redirect('my_listings')
    return render(request, 'ads/delete_listing.html', {'listing': listing})

