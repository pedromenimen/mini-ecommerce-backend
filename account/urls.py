from django.urls import path

import account.views as views

urlpatterns = [
    path("users/login/", views.LoginView.as_view()),
    path("users/register/", views.CreateUserView.as_view()),
]
