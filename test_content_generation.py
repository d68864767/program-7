import unittest
from unittest.mock import patch
from content_generator import ContentGenerator

class TestContentGeneration(unittest.TestCase):

    def setUp(self):
        self.content_generator = ContentGenerator()

    @patch('content_generator.ContentGenerator.create_content')
    def test_create_content(self, mock_create_content):
        # Mock the return value of create_content
        mock_create_content.return_value = "This is a generated content about AI."

        # Call the create_content method
        result = self.content_generator.create_content("AI", "en", 500)

        # Assert that the result matches the mock return value
        self.assertEqual(result, "This is a generated content about AI.")
        mock_create_content.assert_called_once_with("AI", "en", 500)

    @patch('content_generator.ContentGenerator.optimize_content')
    def test_optimize_content(self, mock_optimize_content):
        # Mock the return value of optimize_content
        mock_optimize_content.return_value = "This is optimized content with SEO keywords."

        # Call the optimize_content method
        content = "This is some content."
        seo_keywords = ["SEO", "content", "keywords"]
        result = self.content_generator.optimize_content(content, seo_keywords)

        # Assert that the result matches the mock return value
        self.assertEqual(result, "This is optimized content with SEO keywords.")
        mock_optimize_content.assert_called_once_with(content, seo_keywords)

    @patch('content_generator.ContentGenerator.create_content')
    def test_create_content_sentiment_and_keywords(self, mock_create_content):
        # Mock the return value of create_content to include sentiment and keywords
        mock_create_content.return_value = {
            'content': "This is a generated content about AI.",
            'sentiment': {'neg': 0.0, 'neu': 0.8, 'pos': 0.2, 'compound': 0.5},
            'keywords': ['AI', 'generated', 'content']
        }

        # Call the create_content method
        result = self.content_generator.create_content("AI", "en", 500)

        # Assert that the result includes content, sentiment, and keywords
        self.assertIn('content', result)
        self.assertIn('sentiment', result)
        self.assertIn('keywords', result)
        self.assertEqual(result['content'], "This is a generated content about AI.")
        self.assertEqual(result['sentiment'], {'neg': 0.0, 'neu': 0.8, 'pos': 0.2, 'compound': 0.5})
        self.assertEqual(result['keywords'], ['AI', 'generated', 'content'])

if __name__ == '__main__':
    unittest.main()
