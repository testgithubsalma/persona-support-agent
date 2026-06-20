import os

DATA_FOLDER = "data"

def retrieve_documents(query):
    docs = []

    for file in os.listdir(DATA_FOLDER):
        docs.append(file)

    return docs[:3]