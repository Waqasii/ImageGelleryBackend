import graphene


class CreateImageArguments(graphene.InputObjectType):
    user_id = graphene.ID(required=False)
    image_url = graphene.String(required=True)
    image_filename = graphene.String(required=True)
    thumbnail_url = graphene.String(required=False)
    thumbnail_filename = graphene.String(required=False)


class DeleteImageArguments(graphene.InputObjectType):
    image_filename = graphene.String(required=True)
