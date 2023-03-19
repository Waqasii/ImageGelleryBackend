import graphene
from gallery.types.types import UserType, ImageType
from gallery.models import User, Image


class Query(graphene.ObjectType):
    """
    The root query object of the GraphQL schema.
    """
    # User model queries
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.Int(required=True))

    # Image model queries
    all_images = graphene.List(ImageType)
    image_by_user = graphene.List(
        ImageType, user_id=graphene.Int(required=True))

    def resolve_all_users(root, info):
        """
        Return all available user data 

        Args:
            None

        Returns:
            Object: It will return the object that contain all the user info (USER MODEL)
        """
        return User.objects.all()

    def resolve_user_by_id(root, info, user_id):
        """
        Return user data with specific ID, provided in parameter

        Args:
            user_id (int): Id of user to fetch all his data

        Returns:
            Object: It will return the object that contain all the user info (USER MODEL)
        """
        try:
            return User.objects.get(id=user_id)
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

    def resolve_image_by_user(root, info, user_id):
        """
        Return all images associated with specific user

        Args:
            user_id (int): Id of user to fetch all his images

        Returns:
            Object: It will return the object that contain all the user and his associated images info
        """
        try:
            return (User.objects.get(id=user_id)).images.all()
        except User.DoesNotExist:
            return ValueError("User doesn't Exist!")
