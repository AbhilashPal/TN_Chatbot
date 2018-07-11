import gensim
from gensim.models import KeyedVectors
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

wv_embeddings = KeyedVectors.load_word2vec_format('D:/Machine Learning/NLP/natural-language-processing-master/week3/data/vector.bin', binary=True,limit=500000)

def query_to_vec(query,embeddings,dim=300):
    embed = [embeddings[word] for word in query.split(" ") if word in embeddings]
    if not embed:
        return np.zeros(dim)
    return np.array(embed)

def contains(x,y):
    for i in x.split(" "): 
        if i in wv_embeddings:
            if cosine_similarity(wv_embeddings[i].reshape(1, -1),wv_embeddings[y].reshape(1, -1)) > 0.40 : 
                return True
    return False

#this function checks if make project intent is present in the sentence
def checkforproject(x):
    if contains(x,'create') and contains(x,'project'):
        return True
    return False

#this function checks if make table intent is present in the sentence
def checkfortable(x):
    if contains(x,'create') and contains(x,'table'):
        return True
    return False

#this function checks if make column intent is present in the sentence
def checkforcolumn(x):
    if contains(x,'create') and contains(x,'column'):
        return True
    return False

#this function checks if affirmative intent is present in the sentence
def checkforYes(x):
    if contains(x,'yes'):
        return True
    return False

#this function checks if hi! intent is present in the sentence
def checkforhi(x):
    if contains(x,'hi') or contains(x,"hello"):
        return True
    return False

def checkforpkey():
    x = input("Do you want this to be a primary key ? \n>>>")
    if checkforYes(x):
        return True
    return False

#entering non empty string    
def enternonempty():
    x = input(">>>")
    while x=="":
        print("Name cannot be NULL. Please Re-enter.")
        x = input(">>>")
    return x

    
def desc(pname,MainJSON,pf,tf,cf):
    #describing data collected
    print("Data Collected for Json : ")
    print("Projects Created :",pname)
    print("JSON Data Created :",MainJSON)

    print("No of Projects:",pf)
    print("No of Tables:",tf)
    print("No of Column:",cf)

def encode_json(MainJSON):
    json_data = json.dumps(MainJSON)
    return json_data