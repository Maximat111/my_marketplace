from django.contrib import admin
from django.urls import path, include
from ads import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),  # Підключення додатку ads
    path('', views.welcome, name='welcome'),  # Кореневий маршрут

    # Авторизація
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Реєстрація
    path('register/', views.register, name='register'),

    path('create/', views.create_listing, name='create_listing'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

