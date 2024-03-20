from flask import Flask, jsonify, render_template, request
from summarize import text_summarize
from waitress import serve
from flask_pymongo import PyMongo
import time
import os

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://localhost:27017/summaries"
app.config['MONGO_URI'] = "mongodb+srv://pranamika:6tmIbyUsGo6D0iX3@summarizer.ev8gtlf.mongodb.net/summarizer"
mongo = PyMongo(app)

@app.route('/')
def app_ui():
    return render_template('text_ui.html')

@app.route('/summarize', methods=['POST'])
def summ():
    data = request.json
    text = data.get('text', '')
    summary = text_summarize(text)
    ts = time.time()
    mongo.db.summary.insert_one({"timestamp": ts, "summarized": summary})
    return jsonify({'summary': summary})

if __name__ == '__main__':
    serve(app, host="localhost", port=3000)