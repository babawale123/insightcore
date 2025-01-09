from django.urls import path
from .views import SignIn,SignupView

urlpatterns = [
    path("",SignupView.as_view()),
    path("login/", SignIn.as_view())
]