
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home-page"),  
    path("adduser/",views.adduser,name="add-user"),
    path("adduser/userdb/",views.userdb,name="add-user-db"),
    path("delete/<int:id>",views.deletedata,name="del-data"),
    path("edit/<int:id>",views.editdata,name="edit-page"),
    path("edit/update/",views.update,name="update-data"),
]
