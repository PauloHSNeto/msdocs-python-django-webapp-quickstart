from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.registro_do_animal, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('update_record/<int:pk>', views.update_animal, name='update_record'),
    path('pet_list/', views.pet_list, name='pet_list'),
    path('animal_profile/<int:pk>', views.animal_profile, name='animal_profile'),
]