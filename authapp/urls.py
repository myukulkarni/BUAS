from django.urls import path
from .views import register_view, index, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Include additional paths for login, logout, etc. as needed
]
