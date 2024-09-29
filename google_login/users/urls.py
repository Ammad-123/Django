from django.urls import path
from users import views

urlpatterns = [
    path("",views.home),
    path("logout",views.logout_view)

]