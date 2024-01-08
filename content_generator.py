import os
from ai_core import AICore
from nlp_utils import NLPUtils
from data_handler import DataHandler
from text_analyzer import TextAnalyzer

class ContentGenerator:
    def __init__(self):
        self.ai_core = AICore()
        self.data_handler = DataHandler()
        self.text_analyzer = TextAnalyzer()

    def create_content(self, topic, language=None, max_tokens=None):
        """
        Create content based on a given topic using AI-powered text generation.

        :param topic: The topic or title for the content to be generated.
        :param language: The language in which to generate the content.
        :param max_tokens: The maximum number of tokens to generate.
        :return: The generated content as a string.
        """
        # Generate a prompt for the AI to create content
        prompt = f"Write a detailed, informative, and engaging article about {topic}:"

        # Generate text using the AI core
        generated_text = self.ai_core.generate_text(prompt, language, max_tokens)

        # Analyze the sentiment of the generated text
        sentiment = self.text_analyzer.analyze_sentiment(generated_text)

        # Extract keywords from the generated text
        keywords = NLPUtils.extract_keywords(generated_text)

        # Save the generated content to a file
        content_data = {
            'topic': topic,
            'content': generated_text,
            'sentiment': sentiment,
            'keywords': keywords
        }
        self.data_handler.save_data(f"{topic.replace(' ', '_')}.json", content_data)

        return generated_text

    def optimize_content(self, content, seo_keywords=None):
        """
        Optimize the given content for SEO by including specified keywords.

        :param content: The content to be optimized.
        :param seo_keywords: A list of SEO keywords to include in the content.
        :return: The optimized content as a string.
        """
        if not seo_keywords:
            seo_keywords = os.getenv('SEO_KEYWORDS', '').split(',')

        # Simple optimization by ensuring keywords are included in the content
        for keyword in seo_keywords:
            if keyword.lower() not in content.lower():
                content += f" {keyword}"

        return content

# Example usage
if __name__ == "__main__":
    content_gen = ContentGenerator()
    topic = "The Future of AI in Content Generation"
    generated_content = content_gen.create_content(topic)
    optimized_content = content_gen.optimize_content(generated_content, ['AI', 'content generation', 'technology'])
    print(optimized_content)
