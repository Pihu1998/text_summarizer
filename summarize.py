from transformers import pipeline
import os

llm = pipeline("summarization")
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "1"

def text_summarize(article):
    summary = llm(article, max_length=130, min_length=30, do_sample=True)
    text = summary[0]['summary_text']
    return text

if __name__ == '__main__':
    pass