from django.urls import path
from.import views

urlpatterns = [
    path("",views.home , name = "home"),
    path("animal_list_filter",views.animal_list_filter , name = "animal_list_filter"),
    path("add_new_animal",views.add_new_animal , name = "add_new_animal"),
    path("delete_animal",views.delete_animal , name = "delete_animal")
]