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
    image_url = models.URLField(
        max_length=200,
        verbose_name='Image URL',
        default="https://www.lifewire.com/thmb/5Y8ggTdQiyLdq9us-IMpsACJP-s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/alert-icon-5807a14f5f9b5805c2aa679c.PNG"
    )
    thumbnail_url = models.URLField(
        max_length=200,
        verbose_name='Thumbnail URL',
        default="https://www.lifewire.com/thmb/5Y8ggTdQiyLdq9us-IMpsACJP-s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/alert-icon-5807a14f5f9b5805c2aa679c.PNG"

    )
    image_filename = models.CharField(
        max_length=200,
        verbose_name='Image Filename',
        default="error_image"
    )
    thumbnail_filename = models.CharField(
        max_length=200,
        verbose_name='Thumbnail Filename',
        default="error_thumbnail"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
