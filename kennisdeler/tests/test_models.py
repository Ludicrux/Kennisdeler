from unittest.mock import patch

from django.core.files import File
from django.test import TestCase
from django.contrib.auth import get_user_mode
from django.core.files.uploadedfile import SimpleUploadedFile

import mock

from articles import models


def create_mock_file(file_name):
    """Create a mockfile for tests"""
    mock_file = mock.MagicMock()
    mock_file.name = file_name
    return mock_file

def sample_user(email='test@go2people.nl', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ArticleModelTests(TestCase):
    """Unit tests for models"""
    
    def setUp(self):
        """Test the article string representation"""
        self.article = models.Article.obkects.create(
            title="Grave digger",
            author=sample_user(),
            short_desc="this is a test",
            image=create_mock_file('testimage.png')
            uploaded_file=create_mock_file('testdocument.pdf')
        )

    def test_article_str(self):
        """Test the article string representation"""
        self.assertEqual(str(self.article), article.title)
        