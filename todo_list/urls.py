from django.urls import path
from .views import home, about, delete, completed, uncompleted, edit

urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name="about"),
    path('delete/<list_id>', delete, name = "delete"),
    path('completed/<list_id>', completed, name = 'completed'),
    path('uncompleted/<list_id>', uncompleted, name = 'uncompleted'),
    path('edit/<list_id>', edit, name = 'edit'),

]
