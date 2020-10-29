"""Unit test for article model"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from articles.models import Article, Subject, Tag
from users.models import User, Profile


image_path = "test-images/test_image.jpeg"
test_image = SimpleUploadedFile(
    name='test_image.jpg',
    content=open(image_path, 'rb').read(),
    content_type='image/jpeg'
)


class ArticleModelTest(TestCase):
    """Test the article model"""
    def setUpTestData(self):
        user1 = User.objects.create(
            first_name="Test",
            last_name="User",
            email="Test@user.com",
        )
        profile1 = Profile.objects.create(
            user=user1,
            job="Docent Timmeren",
            organization="ROC",
            profile_picture=test_image
        )
        tag1 = Tag.objects.create(name="TestTag")
        subject1 = Subject.objects.create(name="TestSubject", image=test_image)
        Article.objects.create(
            title="Test Article",
            author=user1,
            short_desc="this is a test article",
            image=test_image,
            subject=subject1,
            tag=tag1
        )
