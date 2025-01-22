from django.test import TestCase
from django.contrib.auth.models import User
from quiz.models import Profile as QuizProfile
from account.models import Profile as AccountProfile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        QuizProfile.objects.create(user=self.user)
        AccountProfile.objects.create(user=self.user)

    def test_profiles(self):
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user.quiz_profile)
        self.assertIsNotNone(user.account_profile)
