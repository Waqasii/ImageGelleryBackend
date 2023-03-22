import graphene
from gallery.types.types import UserType, ImageType
from gallery.models import User, Image
from graphql_auth.schema import UserQuery, MeQuery
from django.db.models import Count


class Query(UserQuery, MeQuery, graphene.ObjectType):
    """
    The root query object of the GraphQL schema.
    """
    # User model queries
    all_users = graphene.List(UserType)

    # Image model queries
    all_images = graphene.List(ImageType)

    images_by_user = graphene.List(ImageType)  # for grid view

    user_info = graphene.Field(UserType)  # for Header

    def resolve_all_users(root, info):
        """
        Return all available user data 

        Args:
            None

        Returns:
            Object: It will return the object that contain all the user info (USER MODEL)
        """
        return User.objects.all()

    def resolve_user_info(root, info):
        """
        Return user data with specific ID, provided in parameter

        Args:
            user_id (int): Id of user to fetch all his data

        Returns:
            Object: It will return the object that contain all the user info (USER MODEL)
        """
        # id=info.context.user.id
        try:
            return User.objects.get(id=info.context.user.id)

        except User.DoesNotExist:
            return ValueError("User doesn't Exist!")

    def resolve_all_images(root, info):
        """
        Return all images 

        Args:
            None

        Returns:
            Object: It will return all the available images in db
        """
        return Image.objects.all()

    def resolve_images_by_user(root, info):
        """
        Return all images associated with specific user

        Args:
            root, info

        Returns:
            Object: It will return the object that contain all the user and his associated images info
        """
        try:
            return (User.objects.get(id=info.context.user.id)).images.all()
        except User.DoesNotExist:
            return ValueError("User doesn't Exist!")
