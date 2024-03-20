from transformers import pipeline
import os

# Import summarization pipeline
llm = pipeline("summarization")
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "1"

# Summarise the input article text
def text_summarize(article: str) -> str:
    # Specify max and min length of summarised output
    summary = llm(article, max_length=130, min_length=30, do_sample=True)
    text = summary[0]['summary_text']
    return text

if __name__ == '__main__':
    pass