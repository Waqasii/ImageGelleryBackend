import graphene
from graphene_django import DjangoObjectType
from gallery.models import User, Image


class UserType(DjangoObjectType):
    total_pictures = graphene.Int(required=True)

    class Meta:
        model = User
        exclude = ("password", )

    def resolve_total_pictures(self, info):
        return self.images.count()


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = "__all__"
