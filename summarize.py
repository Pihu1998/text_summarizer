from transformers import pipeline

llm = pipeline("summarization")

def text_summarize(article):
    summary = llm(article, max_length=130, min_length=30, do_sample=True)
    text = summary[0]['summary_text']
    return text

if __name__ == '__main__':
    pass
#     article = """
#     LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, chatbots, and code analysis.[2]

#     History
#     LangChain was launched in October 2022 as an open source project by Harrison Chase, while working at machine learning startup Robust Intelligence. The project quickly garnered popularity,[3] with improvements from hundreds of contributors on GitHub, trending discussions on Twitter, lively activity on the project's Discord server, many YouTube tutorials, and meetups in San Francisco and London. In April 2023, LangChain had incorporated and the new startup raised over $20 million in funding at a valuation of at least $200 million from venture firm Sequoia Capital, a week after announcing a $10 million seed investment from Benchmark.[4][5]

#     In October 2023 LangChain introduced LangServe, a deployment tool designed to facilitate the transition from LCEL (LangChain Expression Language) prototypes to production-ready applications.[6]

#     Capabilities
#     LangChain's developers highlight the framework's applicability to use-cases including chatbots,[7] retrieval-augmented generation,[8] document summarization,[9] and synthetic data generation.[10]

#     As of March 2023, LangChain included integrations with systems including Amazon, Google, and Microsoft Azure cloud storage; API wrappers for news, movie information, and weather; Bash for summarization, syntax and semantics checking, and execution of shell scripts; multiple web scraping subsystems and templates; few-shot learning prompt generation support; finding and summarizing "todo" tasks in code; Google Drive documents, spreadsheets, and presentations summarization, extraction, and creation; Google Search and Microsoft Bing web search; OpenAI, Anthropic, and Hugging Face language models; iFixit repair guides and wikis search and summarization; MapReduce for question answering, combining documents, and question generation; N-gram overlap scoring; PyPDF, pdfminer, fitz, and pymupdf for PDF file text extraction and manipulation; Python and JavaScript code generation, analysis, and debugging; Milvus vector database[11] to store and retrieve vector embeddings; Weaviate vector database[12] to cache embedding and data objects; Redis cache database storage; Python RequestsWrapper and other methods for API requests; SQL and NoSQL databases including JSON support; Streamlit, including for logging; text mapping for k-nearest neighbors search; time zone conversion and calendar operations; tracing and recording stack symbols in threaded and asynchronous subprocess runs; and the Wolfram Alpha website and SDK.[13] As of April 2023, it can read from more than 50 document types and data sources.[14]
#     """
#     summary = text_summarize(article)
#     print(summary)

