import os
from dotenv import load_dotenv
from nlp_utils import NLPUtils
from text_analyzer import TextAnalyzer

# Load environment variables from .env file
load_dotenv()

class ContentOptimizer:
    def __init__(self):
        self.seo_keywords = os.getenv('SEO_KEYWORDS', '').split(',')
        self.text_analyzer = TextAnalyzer()

    def optimize_for_seo(self, content, target_keywords=None):
        """
        Optimize the given content for SEO by ensuring target keywords are included.

        :param content: The content to be optimized.
        :param target_keywords: A list of keywords to target for SEO optimization.
        :return: The optimized content.
        """
        if target_keywords is None:
            target_keywords = self.seo_keywords

        # Extract current keywords from content
        current_keywords = NLPUtils.extract_keywords(content)

        # Check if target keywords are in current keywords and add them if not
        for keyword in target_keywords:
            if keyword.lower() not in (kw.lower() for kw in current_keywords):
                content += f" {keyword}"

        return content

    def enhance_readability(self, content):
        """
        Enhance the readability of the content by checking grammar and sentence structure.

        :param content: The content to be enhanced.
        :return: The content with improved readability.
        """
        # This is a placeholder for readability enhancement logic
        # In a real-world scenario, this could involve complex NLP operations
        # and integration with third-party services for grammar checking.
        return content

    def analyze_and_improve_sentiment(self, content):
        """
        Analyze the sentiment of the content and make improvements if necessary.

        :param content: The content to be analyzed and improved.
        :return: The content with improved sentiment.
        """
        sentiment_score = self.text_analyzer.analyze_sentiment(content)
        if sentiment_score['compound'] < 0.05:
            # This is a placeholder for sentiment improvement logic
            # In a real-world scenario, this could involve rephrasing negative sentences
            # or adding positive statements to the content.
            content += "\nWe hope you enjoy this content!"

        return content

    def optimize_content(self, content, target_keywords=None):
        """
        Perform a full optimization on the content including SEO, readability, and sentiment.

        :param content: The content to be optimized.
        :param target_keywords: A list of keywords to target for SEO optimization.
        :return: Fully optimized content.
        """
        content = self.optimize_for_seo(content, target_keywords)
        content = self.enhance_readability(content)
        content = self.analyze_and_improve_sentiment(content)
        return content

# Example usage:
# optimizer = ContentOptimizer()
# optimized_content = optimizer.optimize_content("Here is some sample content to optimize.", ["sample", "optimize"])
# print(optimized_content)
