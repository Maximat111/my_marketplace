from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import listing_list

urlpatterns = [
    path('listings/', views.listing_list, name='listing_list'),  # Головна сторінка зі списком оголошень
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),  # Деталі одного оголошення
    path('dashboard/', views.dashboard, name='dashboard'),  # Панель навігації
    path('my_listings/', views.my_listings, name='my_listings'),
    path('create/', views.create_listing, name='create_listing'),
    path('edit/<int:pk>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:pk>/', views.delete_listing, name='delete_listing'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
