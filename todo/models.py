from django.contrib.auth.models import AbstractUser
from todo.manager import CustomUserManager
from django.db import models
from django.conf import settings

# Create your models here.

'''
A custom User model that makes the email field required and unique instead of the Username field
'''

class CustomUser(AbstractUser):
    """User model."""

    username = models.CharField(max_length=100)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class TodoItem(models.Model):

    # Todo Item Models

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="todo_item")
    name = models.CharField(max_length = 100)
    is_completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "todo_items"

    def __str__(self) -> str:
        return self.name
