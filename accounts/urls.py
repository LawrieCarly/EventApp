from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name="accounts_login"),
    path('logout/', LogoutView.as_view(next_page="/"), name="accounts_logout"),
    path('register/', views.register, name='accounts_register')
]
