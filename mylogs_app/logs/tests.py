from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='Test@1234')
        self.assertEqual(user.email, 'test@example.com')

# Create your tests here.
