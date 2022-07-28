from sentence_transformers import SentenceTransformer, util
import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')

model = SentenceTransformer('stsb-roberta-large')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def run_model (input, query):
    # text_file = open('text/ECON175 Essay #2.txt','r')
    # data = text_file.read()
    corpus = tokenizer.tokenize(input)

    # encode corpus to get corpus embeddings
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

    # sentence = "venezuela's future"
    # encode sentence to get sentence embeddings
    sentence_embedding = model.encode(query, convert_to_tensor=True)
    # top_k results to return
    top_k=5
    # compute similarity scores of the sentence with the corpus
    cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
    # Sort the results in decreasing order and get the first top_k
    top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
    print("Sentence:", query, "\n")
    print("Top", top_k, "most similar sentences in corpus:")

    res = []
    for idx in top_results[0:top_k]:
        res_str = corpus[idx], "(Score: %.4f)" % (cos_scores[idx])
        res.append(res_str)
    
    return res