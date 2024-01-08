import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class TextAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the given text using VADER sentiment analysis.
        :param text: str
        :return: dict
        """
        return self.sentiment_analyzer.polarity_scores(text)

    def get_subjectivity(self, text):
        """
        Get the subjectivity score of the given text using TextBlob.
        :param text: str
        :return: float
        """
        return TextBlob(text).sentiment.subjectivity

    def get_readability_score(self, text):
        """
        Calculate the readability score of the given text using a suitable formula.
        :param text: str
        :return: float
        """
        # Implement a readability score calculation (e.g., Flesch–Kincaid)
        # This is a placeholder for the actual implementation
        return 0.0  # Placeholder value

    def summarize_text(self, text, summary_length=100):
        """
        Summarize the given text to the specified summary length.
        :param text: str
        :param summary_length: int
        :return: str
        """
        # Implement a text summarization algorithm or use an existing library
        # This is a placeholder for the actual implementation
        return text[:summary_length]  # Placeholder for the actual summary

    def extract_keywords(self, text, top_n=5):
        """
        Extract keywords from the given text.
        :param text: str
        :param top_n: int
        :return: list
        """
        # Implement a keyword extraction method or use an existing library
        # This is a placeholder for the actual implementation
        return text.split()[:top_n]  # Placeholder for the actual keywords

    def get_word_count(self, text):
        """
        Count the number of words in the given text.
        :param text: str
        :return: int
        """
        words = re.findall(r'\w+', text)
        return len(words)

    def get_character_count(self, text):
        """
        Count the number of characters in the given text.
        :param text: str
        :return: int
        """
        return len(text)

    def get_sentence_count(self, text):
        """
        Count the number of sentences in the given text.
        :param text: str
        :return: int
        """
        sentences = re.split(r'[.!?]+', text)
        return len(sentences) - 1  # Adjust for the last split

# Example usage:
# analyzer = TextAnalyzer()
# sentiment = analyzer.analyze_sentiment("I love programming with AI!")
# subjectivity = analyzer.get_subjectivity("I love programming with AI!")
# readability = analyzer.get_readability_score("I love programming with AI!")
# summary = analyzer.summarize_text("I love programming with AI!", summary_length=5)
# keywords = analyzer.extract_keywords("I love programming with AI!", top_n=3)
# word_count = analyzer.get_word_count("I love programming with AI!")
# character_count = analyzer.get_character_count("I love programming with AI!")
# sentence_count = analyzer.get_sentence_count("I love programming with AI!")
