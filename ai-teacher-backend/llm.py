import os, settings
import textwrap
import chromadb
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, Response
from flask_cors import CORS  # Import the CORS library
import google.generativeai as genai
import google.ai.generativelanguage as glm
app = Flask(__name__)
CORS(app) 
genai.configure(api_key=settings.config['google_key'])
model = 'models/embedding-001'
def read_file(file_path, chunk_size=9000):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
def create_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            chunks = read_file(file_path)
            for i, chunk in enumerate(chunks):
                document = {
                    "title": f"{filename} part {i+1}",
                    "content": chunk
                }
                documents.append(document)
    return documents
documents = create_documents('transcriptions')

df = pd.DataFrame(documents)
df.columns = ['Title', 'Text']
df
# Get the embeddings of each text and add to an embeddings column in the dataframe
def embed_fn(title, text, chunk_size=9000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = []
    for chunk in chunks:
        embedding = genai.embed_content(model=model,
                                        content=chunk,
                                        task_type="retrieval_document",
                                        title=title)["embedding"]
        embeddings.append(embedding)
    return np.mean(embeddings, axis=0)
df['Embeddings'] = df.apply(lambda row: embed_fn(row['Title'], row['Text']), axis=1)
df


model = 'models/embedding-001'


def find_best_passage(query, dataframe):
  """
  Compute the distances between the query and each document in the dataframe
  using the dot product.
  """
  query_embedding = genai.embed_content(model=model,
                                        content=query,
                                        task_type="retrieval_query")
  dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
  idx = np.argmax(dot_products)
  return dataframe.iloc[idx]['Text'] # Return text from index with max value

def make_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = textwrap.dedent("""Do your best to answer this as concisely as possible  \
  If the passage is irrelevant to the answer, try your best to answer it using information provided by the passage.
  QUESTION: '{query}'
  PASSAGE: '{relevant_passage}'

    ANSWER:
  """).format(query=query, relevant_passage=escaped)

  return prompt

@app.route('/run_agent', methods=['POST'])
def run_agent():
    input_text = request.args.get('input_text')
    query = input_text
    print(query)
    passage = find_best_passage(query, df)
    prompt = make_prompt(query, passage)
    print(prompt)
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(prompt)
    print(answer.text)
    return (answer.text)        

if __name__ == '__main__':
    app.run(debug=True, port=5051)
