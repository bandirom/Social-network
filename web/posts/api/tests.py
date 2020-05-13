from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import ArticleModel

User = get_user_model()


class BlogAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', email='test@test.com')
        user.set_password("randompassword")
        user.save()
        article = ArticleModel.objects.create(author=user,
                                              title='new title',
                                              content_full='full')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = ArticleModel.objects.count()
        self.assertEqual(post_count, 1)
