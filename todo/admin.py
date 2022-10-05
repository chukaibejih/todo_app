from django.contrib import admin
from todo.models import TodoItem, CustomUser

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(CustomUser)
