from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('./model')

data = pd.read_csv('transformed_data.csv')
data_array = np.array(data)

encodes = data["encode"]


def string_encode_to_array(string_encode):

    string_encode = string_encode.replace("[", "")
    string_encode = string_encode.replace("]", "")
    string_encode = string_encode.split(" ")

    for i in range(len(string_encode)):
        string_encode[i] = string_encode[i].strip()

    return np.array([float(i) for i in string_encode if i != ''])


def get_max_similarity(text, encodes=encodes):

    encoded_text = model.encode(text)

    all_sims = []

    for encode in encodes:
        encode = string_encode_to_array(encode)
        sim_encodes = cosine_similarity(encode.reshape(1, -1), encoded_text.reshape(1,-1))[0][0]
        all_sims.append(sim_encodes)

    max_value = max(all_sims)
    index = all_sims.index(max_value)

    return index


def get_most_similar(text, data=data, encodes=encodes):

    index = get_max_similarity(text, encodes=encodes)

    question = data.iloc[index]["sentence"]
    link = data.iloc[index]["link"]

    return question, link


if __name__ == "__main__":

    while True:

        text = input("Enter a sentence: ")
        question, link = get_most_similar(text)

        print("Most similar question: ", question)
        print("Awnser: ", link)