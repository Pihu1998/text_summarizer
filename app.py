from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import OpenAI
import streamlit as st
import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values(".env")
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "1"

llm = OpenAI(temperature=0)

def summarize(text):
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(text)
    return summary

if __name__ == '__main__':
    text = """
    In software, a data access object (DAO) is a pattern that provides an abstract interface to some type of database or other persistence mechanism. By mapping application calls to the persistence layer, the DAO provides data operations without exposing database details. This isolation supports the single responsibility principle. It separates the data access the application needs, in terms of domain-specific objects and data types (the DAO's public interface), from how these needs can be satisfied with a specific DBMS (the implementation of the DAO).

Although this design pattern is applicable to most programming languages, most software with persistence needs, and most databases, it is traditionally associated with Java EE applications and with relational databases (accessed via the JDBC API because of its origin in Sun Microsystems' best practice guidelines[1] "Core J2EE Patterns".

Advantages

This section does not cite any sources. Please help improve this section by adding citations to reliable sources. Unsourced material may be challenged and removed. (February 2015) (Learn how and when to remove this template message)
Using data access objects (DAOs) offers a clear advantage: it separates two parts of an application that don't need to know about each other. This separation allows them to evolve independently. If business logic changes, it can rely on a consistent DAO interface. Meanwhile, modifications to persistence logic won't affect DAO clients.

All details of storage are hidden from the rest of the application (see information hiding). Unit testing code is facilitated by substituting a test double for the DAO in the test, thereby making the tests independent of the persistence layer.

In the context of the Java programming language, DAO can be implemented in various ways. This can range from a fairly simple interface that separates data access from the application logic, to frameworks and commercial products.

Technologies like Java Persistence API and Enterprise JavaBeans come built into application servers and can be used in applications that use a Java EE application server. Commercial products such as TopLink are available based on object–relational mapping (ORM). Popular open source ORM software includes Doctrine, Hibernate, iBATIS and JPA implementations such as Apache OpenJPA.[2]

Disadvantages
Potential disadvantages of using DAO include leaky abstraction,[citation needed] code duplication, and abstraction inversion. In particular, the abstraction of the DAO as a regular Java object can obscure the high cost of each database access. Developers may inadvertently make multiple database queries to retrieve information that could be returned in a single operation. If an application requires multiple DAOs, the same create, read, update, and delete code may have to be written for each DAO.[3]

    """
    summary = summarize(text)
    print("Summary\n")
    print(summary)