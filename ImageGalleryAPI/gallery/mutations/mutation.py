import graphene
from gallery.types.types import ImageType
from gallery.models import Image, User
from graphql_auth import mutations
from graphql_jwt.decorators import login_required
from gallery.types.inputs import CreateImageArguments, DeleteImageArguments
from gallery.helpers.utils import thumbnail_filename_url_creator
# from graphql_jwt import mutations


class CreateUpdateImage(graphene.Mutation):
    class Arguments:
        input_data = CreateImageArguments(required=True)

    # The class attributes define the response of the mutation
    image = graphene.Field(ImageType)

    @classmethod
    @login_required
    def mutate(cls, root, info, input_data):
        """
        Add/update image for given user if exist

        Args:
            image_url (str): URL of image return by s3,
            image_filename (str): Input image file name
            thumbnail_url (str): Thumbnail url if available else we gonna make it ourselves here,
            thumbnail_filename (str): Thumbnail filename if available else we gonna make it ourselves here,

        Returns:
            Object: It will return the object that contain all the newly created Image info (Image MODEL)
        """

        user = User.objects.get(id=info.context.user.id)
        if (not (input_data.thumbnail_url or input_data.thumbnail_filename)):
            input_data.thumbnail_filename, input_data.thumbnail_url = thumbnail_filename_url_creator(
                filename=input_data.image_filename, fileurl=input_data.image_url)

        obj, created = Image.objects.update_or_create(
            user=user,
            image_filename=input_data.image_filename,
            defaults={
                'image_url': input_data.image_url,
                'thumbnail_url': input_data.thumbnail_url,
                'thumbnail_filename': input_data.thumbnail_filename
            }
        )

        return CreateUpdateImage(image=obj)


class DeleteImage(graphene.Mutation):
    class Arguments:
        input_data = DeleteImageArguments(required=True)

    message = graphene.String()
    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, input_data):
        try:
            image = Image.objects.get(image_filename=input_data.image_filename)
            image.delete()
            return DeleteImage(message='Image deleted successfully!', success=True)
        except Image.DoesNotExist:
            return DeleteImage(message='Image does not exist', success=False)


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()  # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    add_update_image = CreateUpdateImage.Field()
    delete_image = DeleteImage.Field()
