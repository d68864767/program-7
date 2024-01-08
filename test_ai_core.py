import unittest
from ai_core import AICore

class TestAICore(unittest.TestCase):
    def setUp(self):
        """Initialize AICore before each test."""
        self.ai_core = AICore()

    def test_generate_text_with_valid_prompt(self):
        """Test text generation with a valid prompt."""
        prompt = "Hello, world!"
        generated_text = self.ai_core.generate_text(prompt)
        self.assertIsInstance(generated_text, str)
        self.assertTrue(len(generated_text) > 0)

    def test_generate_text_with_empty_prompt(self):
        """Test text generation with an empty prompt."""
        prompt = ""
        with self.assertRaises(ValueError):
            self.ai_core.generate_text(prompt)

    def test_generate_text_with_unsupported_language(self):
        """Test text generation with an unsupported language."""
        prompt = "Hello, world!"
        unsupported_language = "xx"  # Assuming 'xx' is not in the SUPPORTED_LANGUAGES
        with self.assertRaises(ValueError):
            self.ai_core.generate_text(prompt, language=unsupported_language)

    def test_generate_text_with_max_tokens(self):
        """Test text generation with a specific max_tokens value."""
        prompt = "Hello, world!"
        max_tokens = 50
        generated_text = self.ai_core.generate_text(prompt, max_tokens=max_tokens)
        self.assertTrue(len(generated_text.split()) <= max_tokens)

    def test_api_key_set(self):
        """Test that the API key is set."""
        self.assertIsNotNone(self.ai_core.api_key)

    def test_default_language_set(self):
        """Test that the default language is set."""
        self.assertIsNotNone(self.ai_core.default_language)

    def test_max_tokens_set(self):
        """Test that the max tokens value is set."""
        self.assertIsInstance(self.ai_core.max_tokens, int)

if __name__ == '__main__':
    unittest.main()
