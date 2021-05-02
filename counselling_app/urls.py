from django.urls import path
from .views import register, about, dash, login, logout, create_appointment, cancel_appointment

# default path = /
urlpatterns = [
    path('', login, name="login"),
    path('dash/', dash, name="dash"),
    path('register/', register, name="register"),
    path('about/', about, name="about"),
    path('logout/', logout, name="logout"),
    path('create_appointment/', create_appointment, name="create_appointment"),
    path('cancel_appointment/<slug:id>/', cancel_appointment, name="cancel_appointment")
]