import json
from django.contrib.auth import get_user_model
from graphene_django.utils.testing import GraphQLTestCase
from graphene.test import Client
from gallery.schema import schema
from rest_framework.test import APIClient
from graphql_jwt.shortcuts import get_token
from gallery.models import Image


class GraphQLAPITestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.rf_client = APIClient()
        self.user = get_user_model().objects.create(
            username='testuser', email='test@example.com')
        self.rf_client.force_authenticate(user=self.user)

    def tearDown(self):
        self.rf_client.logout()
        self.user.delete()

    def test_create_image_mutation(self):
        # create the JWT token
        token = get_token(self.user)

        # set up the mutation and variables
        mutation = '''
            mutation createImage($input_data: CreateImageArguments!) {
              addUpdateImage(inputData: $input_data) {
                image {
                  id
                  imageUrl
                  imageFilename
                  thumbnailUrl
                  thumbnailFilename
                }
              }
            }
        '''
        variables = {
            "input_data": {
                "imageUrl": "https://example.com/image.jpg",
                "imageFilename": "image24.jpg"
            }
        }

        # make the authenticated request with the JWT token in the Authorization header
        response = self.rf_client.post('/graphql',
                                       json.dumps(
                                           {'query': mutation, 'variables': variables}),
                                       content_type='application/json',
                                       HTTP_AUTHORIZATION=f'JWT {token}')

        # assert the response is successful
        self.assertEqual(response.status_code, 200)

        # assert the image was created successfully
        response_data = json.loads(response.content.decode())
        image_data = response_data['data']['addUpdateImage']['image']
        self.assertEqual(image_data['imageUrl'],
                         'https://example.com/image.jpg')
        self.assertEqual(image_data['imageFilename'], 'image24.jpg')

    def test_delete_image_mutation(self):
        # Create a new image
        image = Image.objects.create(
            image_url="https://example.com/image.jpg",
            thumbnail_url="https://example.com/image-resized.jpg",
            image_filename="image24.jpg",
            thumbnail_filename="image24-resized.jpg",
            user=self.user
        )

        # create the JWT token
        token = get_token(self.user)

        # Prepare the mutation input
        mutation = """
            mutation DeleteImage($input_data: DeleteImageArguments!) {
                deleteImage(inputData: $input_data) {
                    message
                    success
                }
            }
        """
        variables = {"input_data": {"imageFilename": "image24.jpg"}}

        # make the authenticated request with the JWT token in the Authorization header
        response = self.rf_client.post('/graphql',
                                       json.dumps(
                                           {'query': mutation, 'variables': variables}),
                                       content_type='application/json',
                                       HTTP_AUTHORIZATION=f'JWT {token}')

        # Verify the response
        assert response.status_code == 200
        assert "errors" not in response.json()

        # Verify that the image was deleted
        assert not Image.objects.filter(pk=image.pk).exists()

        # Verify the response data
        data = response.json()["data"]["deleteImage"]
        assert data["success"] == True
