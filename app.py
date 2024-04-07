from flask import Flask, jsonify, render_template, request
from summarize import text_summarize
from waitress import serve
from flask_pymongo import PyMongo
import time, datetime
import os
from os.path import join, dirname
from dotenv import dotenv_values, load_dotenv

app = Flask(__name__)

# Access MongoDB Access cluster
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Setup PyMongo instance
mongo = PyMongo(app)
# Create mongo database
db = mongo.db

# Our initial form page
@app.route('/')
def app_ui():
    """
    This function renders the template for the text user interface.

    Returns:
        str: The rendered template for the text user interface.
    """
    return render_template('text_ui.html')

# Endpoint encapsulating AI logic
@app.route('/sum', methods=['POST'])
def summarize():
    """
    This function takes in a JSON object containing text and returns a summarized version of the text.

    Args:
        None

    Returns:
        A JSON object containing the summarized text.

    Raises:
        None
    """
    data = request.json
    text = data.get('text', '')
    summary = text_summarize(text)
    ts = datetime.datetime.now()
    db.summary.insert_one({"timestamp": ts, "summarized": summary})
    return jsonify({'summary': summary})

if __name__ == '__main__':
    serve(app, host="localhost", port=3000)