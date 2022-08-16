from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    # path('login/', views.dashboard_login, name="login"),
    # path('logout/', views.dashboard_logout, name="logout"),
]