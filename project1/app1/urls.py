from django.urls import path
from . import views

urlpatterns = [
    path('hv/',views.home,name='home'),
    path('av/',views.about),
    path('cv/',views.contact),
    path('helpv/',views.help),
    path('login/',views.log_in,name='login'),
    path('sign/',views.sign_up)
]