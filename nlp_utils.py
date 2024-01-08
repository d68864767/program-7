import re
from textblob import TextBlob
from langdetect import detect
import spacy

# Load the English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

class NLPUtils:
    @staticmethod
    def extract_keywords(text):
        """
        Extract keywords from a given text using Spacy's NER (Named Entity Recognition).

        :param text: The input text from which to extract keywords.
        :return: A list of unique keywords.
        """
        doc = nlp(text)
        return list(set([ent.text for ent in doc.ents]))

    @staticmethod
    def detect_language(text):
        """
        Detect the language of the given text using langdetect.

        :param text: The input text whose language needs to be detected.
        :return: A string representing the language code (e.g., 'en' for English).
        """
        return detect(text)

    @staticmethod
    def correct_spelling(text):
        """
        Correct spelling in the given text using TextBlob.

        :param text: The input text with potential spelling errors.
        :return: A string with corrected spelling.
        """
        blob = TextBlob(text)
        return str(blob.correct())

    @staticmethod
    def sentiment_analysis(text):
        """
        Perform sentiment analysis on the given text using TextBlob.

        :param text: The input text to analyze.
        :return: A tuple with polarity and subjectivity scores.
        """
        blob = TextBlob(text)
        return blob.sentiment

    @staticmethod
    def summarize_text(text, summary_length=3):
        """
        Summarize the given text using Spacy's text summarization capabilities.

        :param text: The input text to summarize.
        :param summary_length: The number of sentences for the summary.
        :return: A string representing the summarized text.
        """
        doc = nlp(text)
        sentence_ranks = {}
        for sent in doc.sents:
            sentence_ranks[sent] = sent.ents

        # Sort sentences by the number of entities
        summarized = sorted(sentence_ranks, key=lambda e: len(sentence_ranks[e]), reverse=True)
        return ' '.join([str(s) for s in summarized[:summary_length]])

    @staticmethod
    def clean_text(text):
        """
        Clean the given text by removing special characters and multiple spaces.

        :param text: The input text to clean.
        :return: A string representing the cleaned text.
        """
        # Remove special characters and digits
        text = re.sub("(\\d|\\W)+", " ", text)
        # Remove multiple spaces
        text = ' '.join(text.split())
        return text

# Example usage:
# nlp_utils = NLPUtils()
# keywords = nlp_utils.extract_keywords("Apple Inc. is an American multinational technology company headquartered in Cupertino, California.")
# language = nlp_utils.detect_language("This is a sample text.")
# corrected_text = nlp_utils.correct_spelling("I have a dout in this sentense.")
# sentiment = nlp_utils.sentiment_analysis("I love this product! It's absolutely wonderful.")
# summary = nlp_utils.summarize_text("The quick brown fox jumps over the lazy dog. Dogs are domesticated mammals, not natural wild animals.")
# cleaned_text = nlp_utils.clean_text("This is a sample! text, with; punctuation? and special# characters$")
