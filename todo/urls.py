from django.urls import path
from todo.views import delete_todo, home, register, update_todo, complete_todo, delete_todo

# using Django’s built-in login and logout modules
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(template_name="todo/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="todo/logout.html"), name="logout"),
    path("register/", register, name="register"),

    path("update/todo/<int:pk>/", update_todo, name="update_todo"),
    path("complete/todo/<int:pk>/", complete_todo, name="complete_todo"),
    path("delete/todo/<int:pk>/", delete_todo, name="delete_todo"),

]