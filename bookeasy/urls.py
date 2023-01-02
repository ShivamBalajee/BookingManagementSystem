from django.urls import path
from . import views

urlpatterns=[
    path('login', views.get_login),
    path('signup', views.get_signup),
    path('', views.get_index),
    path('moviepage/<int:movie_id>',views.get_moviepage),
    path('payment/<int:order_id>', views.get_payment),
    path('cancellation', views.get_cancellation),
    path('about', views.get_about)

]