from front_env.api.vagas_client import VagasClient
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

#biblioteca spacy
nlp = spacy.load("pt_core_news_sm")
#stopwords
STOPWORDS = set(stopwords.words('portuguese'))

dicionario_val = {}

def df_vagas():
    vagas = {}
    try:
        vagas = VagasClient.get_vagas()
    except:  
        vagas = {'result':[]}
    return vagas

new_vagas = df_vagas()

print(new_vagas["result"])