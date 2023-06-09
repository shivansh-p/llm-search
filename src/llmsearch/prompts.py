DOLLY_PROMPT_TEMPLATE="""### Instruction:
Use the following pieces of context to answer the question at the end. If answer isn't in the context, say that you don't know, don't try to make up an answer.

### Context: 
---------------
{context}
---------------

### Question: {question}
"""



OPENAI_PROMPT_TEMPLATE = """"Context information is provided below:

### Context: 
---------------------
{context}
---------------------

Given the context information and not prior knowledge, answer the question. If answer isn't in the context, say that you don't know, don't try to make up an answer.

### Question: {question}


"""