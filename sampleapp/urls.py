from . import views

from django.urls import path


urlpatterns = [
    path('', views.HomeAPIView.as_view(), name="home"),
    path('user', views.user_delete, name='user_delete'),
    path('home', views.home, name='home'),
    path('contact', views.contact_page, name='contact')
]