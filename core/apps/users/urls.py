from django.urls import path
from apps.users import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.userLogin, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.userLogout, name="logout"),
]