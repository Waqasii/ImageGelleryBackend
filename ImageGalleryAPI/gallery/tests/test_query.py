from django.test import TestCase
from graphene.test import Client
from gallery.schema import schema
from gallery.models import User, Image
from graphql_jwt.shortcuts import get_token
from rest_framework.test import APIClient
import json


class MergedQueryTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.rf_client = APIClient()

        # Create a user and some images for testing
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )

        self.image1 = Image.objects.create(
            image_url="https://example.com/image.jpg",
            thumbnail_url="https://example.com/image-resized.jpg",
            image_filename="image24.jpg",
            thumbnail_filename="image24-resized.jpg",
            user=self.user
        )

        self.image2 = Image.objects.create(
            image_url="https://example.com/image2.jpg",
            thumbnail_url="https://example.com/image-resized2.jpg",
            image_filename="image242.jpg",
            thumbnail_filename="image24-resized2.jpg",
            user=self.user
        )

        # Force authenticate the client with the created user
        self.rf_client.force_authenticate(user=self.user)

    def test_merged_query(self):
        query = '''
            query MergedQuery {
              userInfo{
                username
                email
                totalPictures
              }
              imagesByUser{
                id
                imageUrl
                imageFilename
                thumbnailFilename
                thumbnailUrl
              }
            }
        '''

        # Create a JWT token
        token = get_token(self.user)

        response = self.rf_client.get(
            '/graphql',
            HTTP_AUTHORIZATION=f'JWT {token}',
            data={'query': query}
        )

        # Ensure that the response contains the expected data
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)['data']

        self.assertEqual(data['userInfo']['username'], self.user.username)
        self.assertEqual(data['userInfo']['email'], self.user.email)
        self.assertEqual(data['userInfo']['totalPictures'],
                         self.user.images.count())

        self.assertEqual(len(data['imagesByUser']), 2)
        self.assertEqual(data['imagesByUser'][0]['id'], str(self.image1.id))
        self.assertEqual(data['imagesByUser'][0]
                         ['imageUrl'], self.image1.image_url)
        self.assertEqual(data['imagesByUser'][0]
                         ['imageFilename'], self.image1.image_filename)
        self.assertEqual(
            data['imagesByUser'][0]['thumbnailFilename'], self.image1.thumbnail_filename)
        self.assertEqual(data['imagesByUser'][0]
                         ['thumbnailUrl'], self.image1.thumbnail_url)

        self.assertEqual(data['imagesByUser'][1]['id'], str(self.image2.id))
        self.assertEqual(data['imagesByUser'][1]
                         ['imageUrl'], self.image2.image_url)
        self.assertEqual(data['imagesByUser'][1]
                         ['imageFilename'], self.image2.image_filename)
        self.assertEqual(
            data['imagesByUser'][1]['thumbnailFilename'], self.image2.thumbnail_filename)
        self.assertEqual(data['imagesByUser'][1]
                         ['thumbnailUrl'], self.image2.thumbnail_url)

    def test_header_data_query(self):
        query = '''
            query HeaderData {
              userInfo{
                username
                email
                totalPictures
              }
            }
        '''

        # Create a JWT token
        token = get_token(self.user)

        response = self.rf_client.get(
            '/graphql',
            HTTP_AUTHORIZATION=f'JWT {token}',
            data={'query': query}
        )

        # Ensure that the response contains the expected data
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)['data']

        self.assertEqual(data['userInfo']['username'], self.user.username)
        self.assertEqual(data['userInfo']['email'], self.user.email)
        self.assertEqual(data['userInfo']['totalPictures'],
                         self.user.images.count())


'''
# Create a new image
self.image1 = Image.objects.create(
    image_url="https://example.com/image.jpg",
    thumbnail_url="https://example.com/image-resized.jpg",
    image_filename="image24.jpg",
    thumbnail_filename="image24-resized.jpg",
    user=self.user
)
self.image2 = Image.objects.create(
    image_url="https://example.com/image2.jpg",
    thumbnail_url="https://example.com/image-resized2.jpg",
    image_filename="image242.jpg",
    thumbnail_filename="image24-resized2.jpg",
    user=self.user
)
'''
