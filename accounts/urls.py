from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("login/",views.login_view,name="login"),
    path("logout/", views.logout_view, name="logout"),
]
