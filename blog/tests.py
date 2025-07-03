from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(title="My test post")
        self.assertEqual(str(post), "My test post")