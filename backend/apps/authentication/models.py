# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# TODO: Implementar User customizado depois
# class User(AbstractUser):
#     """Custom User model extending Django's AbstractUser"""
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     
#     ROLE_CHOICES = [
#         ('admin', 'Admin'),
#         ('manager', 'Manager'),
#         ('user', 'User'),
#     ]
#     
#     role = models.CharField(
#         max_length=20,
#         choices=ROLE_CHOICES,
#         default='user'
#     )
#     
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}" if self.first_name else self.username
