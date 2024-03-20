from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import OpenAI
import streamlit as st
import os
from os.path import join, dirname
from dotenv import dotenv_values, load_dotenv
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "1"

model_name = "gpt-3.5-turbo"

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    model_name=model_name
)

article= """
    In software, a data access object (DAO) is a pattern that provides an abstract interface to some type of database or other persistence mechanism. By mapping application calls to the persistence layer, the DAO provides data operations without exposing database details. This isolation supports the single responsibility principle. It separates the data access the application needs, in terms of domain-specific objects and data types (the DAO's public interface), from how these needs can be satisfied with a specific DBMS (the implementation of the DAO).

Although this design pattern is applicable to most programming languages, most software with persistence needs, and most databases, it is traditionally associated with Java EE applications and with relational databases (accessed via the JDBC API because of its origin in Sun Microsystems' best practice guidelines[1] "Core J2EE Patterns".

Advantages

This section does not cite any sources. Please help improve this section by adding citations to reliable sources. Unsourced material may be challenged and removed. (February 2015) (Learn how and when to remove this template message)
Using data access objects (DAOs) offers a clear advantage: it separates two parts of an application that don't need to know about each other. This separation allows them to evolve independently. If business logic changes, it can rely on a consistent DAO interface. Meanwhile, modifications to persistence logic won't affect DAO clients.

All details of storage are hidden from the rest of the application (see information hiding). Unit testing code is facilitated by substituting a test double for the DAO in the test, thereby making the tests independent of the persistence layer.

In the context of the Java programming language, DAO can be implemented in various ways. This can range from a fairly simple interface that separates data access from the application logic, to frameworks and commercial products.

"""
texts = text_splitter.split_text(article)

docs = [Document(page_content=t) for t in texts]
print(len(docs))

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name=model_name)
prompt_template = """Write a concise summary of the following:


{text}


CONSCISE SUMMARY:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:    
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens = num_tokens_from_string(article, model_name)
print(num_tokens)

from langchain.chains.summarize import load_summarize_chain
import textwrap
from time import monotonic

gpt_35_turbo_max_tokens = 4097
verbose = True

if num_tokens < gpt_35_turbo_max_tokens:
  chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt, verbose=verbose)
else:
  chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=prompt, combine_prompt=prompt, verbose=verbose)

start_time = monotonic()
summary = chain.run(docs)

print(f"Chain type: {chain.__class__.__name__}")
print(f"Run time: {monotonic() - start_time}")
print(f"Summary: {textwrap.fill(summary, width=100)}")



# llm = OpenAI(temperature=0)

# def summarize(text):
#     chain = load_summarize_chain(llm, chain_type="map_reduce")
#     summary = chain.run(text)
#     return summary

# if __name__ == '__main__':
#     text = """
#     In software, a data access object (DAO) is a pattern that provides an abstract interface to some type of database or other persistence mechanism. By mapping application calls to the persistence layer, the DAO provides data operations without exposing database details. This isolation supports the single responsibility principle. It separates the data access the application needs, in terms of domain-specific objects and data types (the DAO's public interface), from how these needs can be satisfied with a specific DBMS (the implementation of the DAO).

# Although this design pattern is applicable to most programming languages, most software with persistence needs, and most databases, it is traditionally associated with Java EE applications and with relational databases (accessed via the JDBC API because of its origin in Sun Microsystems' best practice guidelines[1] "Core J2EE Patterns".

# Advantages

# This section does not cite any sources. Please help improve this section by adding citations to reliable sources. Unsourced material may be challenged and removed. (February 2015) (Learn how and when to remove this template message)
# Using data access objects (DAOs) offers a clear advantage: it separates two parts of an application that don't need to know about each other. This separation allows them to evolve independently. If business logic changes, it can rely on a consistent DAO interface. Meanwhile, modifications to persistence logic won't affect DAO clients.

# All details of storage are hidden from the rest of the application (see information hiding). Unit testing code is facilitated by substituting a test double for the DAO in the test, thereby making the tests independent of the persistence layer.

# In the context of the Java programming language, DAO can be implemented in various ways. This can range from a fairly simple interface that separates data access from the application logic, to frameworks and commercial products.

# Technologies like Java Persistence API and Enterprise JavaBeans come built into application servers and can be used in applications that use a Java EE application server. Commercial products such as TopLink are available based on object–relational mapping (ORM). Popular open source ORM software includes Doctrine, Hibernate, iBATIS and JPA implementations such as Apache OpenJPA.[2]

# Disadvantages
# Potential disadvantages of using DAO include leaky abstraction,[citation needed] code duplication, and abstraction inversion. In particular, the abstraction of the DAO as a regular Java object can obscure the high cost of each database access. Developers may inadvertently make multiple database queries to retrieve information that could be returned in a single operation. If an application requires multiple DAOs, the same create, read, update, and delete code may have to be written for each DAO.[3]

#     """
#     summary = summarize(text)
#     print("Summary\n")
#     print(summary)