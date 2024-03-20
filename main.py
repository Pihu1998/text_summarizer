from flask import Flask, jsonify, render_template, request
from summarize import text_summarize
from waitress import serve
from flask_pymongo import PyMongo
import time
import os
from os.path import join, dirname
from dotenv import dotenv_values, load_dotenv

app = Flask(__name__)

# Access MongoDB Access cluster
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Setup PyMongo instance
mongo = PyMongo(app)

# Our initial form page
@app.route('/')
def app_ui():
    return render_template('text_ui.html')

# Endpoint encapsulating AI logic
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = text_summarize(text)
    ts = time.time()
    mongo.db.summary.insert_one({"timestamp": ts, "summarized": summary})
    return jsonify({'summary': summary})

if __name__ == '__main__':
    serve(app, host="localhost", port=3000)