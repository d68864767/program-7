from flask import Flask, request, render_template, jsonify
from ai_core import AICore
from nlp_utils import NLPUtils
from data_handler import DataHandler
from text_analyzer import TextAnalyzer
from content_generator import ContentGenerator
from content_optimizer import ContentOptimizer
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
app.debug = os.getenv('APP_DEBUG', 'True') == 'True'

# Initialize core components
ai_core = AICore()
nlp_utils = NLPUtils()
data_handler = DataHandler()
text_analyzer = TextAnalyzer()
content_generator = ContentGenerator()
content_optimizer = ContentOptimizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.form.get('prompt')
    language = request.form.get('language')
    max_tokens = request.form.get('max_tokens', type=int)

    try:
        generated_text = ai_core.generate_text(prompt, language, max_tokens)
        return jsonify({'status': 'success', 'generated_text': generated_text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form.get('text')

    try:
        sentiment_result = text_analyzer.analyze_sentiment(text)
        keywords = nlp_utils.extract_keywords(text)
        return jsonify({'status': 'success', 'sentiment': sentiment_result, 'keywords': keywords})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/optimize', methods=['POST'])
def optimize_content():
    text = request.form.get('text')
    seo_keywords = request.form.get('seo_keywords')

    try:
        optimized_text = content_optimizer.optimize_for_seo(text, seo_keywords)
        return jsonify({'status': 'success', 'optimized_text': optimized_text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run()
