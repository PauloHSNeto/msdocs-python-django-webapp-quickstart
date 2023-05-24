from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('accounts/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('delete_animal/<int:pk>', views.delete_animal, name='delete_animal'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('update_animal/<int:pk>', views.update_animal, name='update_animal'),
    path('pet_list/', views.pet_list, name='pet_list'),
    path('animal_profile/<int:pk>', views.animal_profile, name='animal_profile'),
    path('animal_profile/<int:pk>/add_vacina', views.add_vacina, name='add_vacina'),
    path('animal_profile/<int:pk>/vacinas_list', views.vacinas_list, name='vacinas_list'),
    path('update_vacina/<int:pk>', views.update_vacina, name='update_vacina'),
    path('delete_vacina/<int:pk>', views.delete_vacina, name='delete_vacina'),
]