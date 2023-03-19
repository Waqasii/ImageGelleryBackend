import graphene
from gallery.types.types import ImageType
from gallery.models import Image, User


class CreateUpdateImage(graphene.Mutation):
    class Arguments:
        # Inputs arg for the mutation
        user_id = graphene.ID(required=True)
        image_url = graphene.String(required=True)
        image_id = graphene.ID(required=False)

    # The class attributes define the response of the mutation
    image = graphene.Field(ImageType)

    @classmethod
    def mutate(cls, root, info, user_id, image_url, image_id=None):
        """
        Add/update image for given user if exist

        Args:
            user_id (int): Id of user to associate image with
            image_url (str): URL of iamge file

        Returns:
            Object: It will return the object that contain all the newly created Image info (Image MODEL)
        """
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return ValueError("User doesn't Exist!")

        if (image_id):
            try:
                img_obj = Image.objects.get(id=image_id)
                img_obj.url = image_url
                img_obj.save()
            except Image.DoesNotExist:
                return (ValueError("Given Image doesn't Exist!"))
        else:
            img_obj = Image(user=user, url=image_url)
            img_obj.save()

        return CreateUpdateImage(image=img_obj)


class DeleteImage(graphene.Mutation):
    class Arguments:
        image_id = graphene.ID(required=True)

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, image_id):
        try:
            image = Image.objects.get(id=image_id)
            image.delete()
            return DeleteImage(message='Image deleted successfully!')
        except Image.DoesNotExist:
            return DeleteImage(message='Image does not exist')


class Mutation(graphene.ObjectType):
    add_update_image = CreateUpdateImage.Field()
    delete_image = DeleteImage.Field()
