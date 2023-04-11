from django.urls import path
from .views import home, delete_task, update_task

app_name="todo"

urlpatterns = [
    path('', home, name='home'),
    path('update/<slug:slug>/', update_task, name='update_task'),
    path('delete/<slug:slug>/', delete_task, name='delete_task'),
]