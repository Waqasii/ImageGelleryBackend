from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=255)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username


class Image(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='images',
    )
    url = models.URLField(
        max_length=200,
        verbose_name='Image URL',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )

    def __str__(self):
        return f'{self.url} ({self.user.first_name})'
