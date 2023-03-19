import graphene
from graphene_django import DjangoObjectType
from gallery.models import User, Image


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password", )


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = "__all__"
