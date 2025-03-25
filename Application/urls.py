from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.data_collection,name='data_collection'),
    path('task_detail/<int:id>/',views.data_table,name='data_table'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('update_task/<int:id>/',views.update_task,name='update_task'),
]

