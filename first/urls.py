
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home-page"),  
    path("adduser/",views.adduser,name="add-user"),
    path("adduser/userdb/",views.userdb,name="add-user-db"),
]
