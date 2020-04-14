from django.urls import path
from  . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:task_id>/done',views.done_task,name="done_task"),
    path('<int:task_id>/undone',views.undone_task,name="undone_task"),
    path('<int:task_id>/delete',views.delete,name="delete"),
    path('<int:task_id>/edit',views.edit,name="edit"),


]
