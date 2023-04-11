from django.urls import path
from .views import user_login, user_signup, user_logout

app_name = "account"

urlpatterns = [
    path('signup/',user_signup, name='user_signup'),
    path('login/',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
]
