from pdfminer.high_level import extract_text
from nltk.tokenize import word_tokenize
from front_env.machine.constantes import *
import pandas as pd
import spacy



#biblioteca spacy
nlp = spacy.load("pt_core_news_sm")

#função para extrair os dados
def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

#extrach candidates skills
def extract_skills(resume_text):

    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]

    # reading the csv file
    data = pd.read_csv("skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]


#extract vagas pontuação
def extract_vagas_pontuacao(resume_text):
    dict_1 = {}
    dict_2 = {}

    dict_3 = {}
    dict_4 = {}

    dict_5 = {}
    dict_6 = {}

    dict_7 = {}
    dict_8 = {}


    contador = 0
    total_ch = 0

    lista_tokens = []

    tokens = word_tokenize(resume_text)

    for w in tokens: 
        if w not in STOPWORDS: 
            lista_tokens.append(w)

    #match descrição
    for d in DESCRICAO:
        for tk in lista_tokens:
            if d in lista_tokens:
                contador = 1
                dict_1[d] = contador
            if d not in lista_tokens:
                contador = 0
                dict_2[d] = contador
    # match experiencia profissional
    for d in EXPERIENCIA_PROFISSIONAL:
        for tk in lista_tokens:
            if d in lista_tokens:
                contador = 1
                dict_3[d] = contador
            if d not in lista_tokens:
                contador = 0
                dict_4[d] = contador
    # match requisitos
    for d in REQUISITOS:
        for tk in lista_tokens:
            if d in lista_tokens:
                contador = 1
                dict_5[d] = contador
            if d not in lista_tokens:
                contador = 0
                dict_6[d] = contador
    #match perfil
    for d in PERFIL:
        for tk in lista_tokens:
            if d in lista_tokens:
                contador = 1
                dict_7[d] = contador
            if d not in lista_tokens:
                contador = 0
                dict_8[d] = contador
    
    #actualizamos o dicionário
    dict_1.update(dict_2)
    dict_3.update(dict_4)
    dict_5.update(dict_6)
    dict_7.update(dict_8)

    #pegando a pontuação
    for vl in dict_1.keys():
        total_ch = sum(dict_1.values())
    dict_1["pontuação"] = total_ch

    for vl in dict_3.keys():
        total_ch = sum(dict_3.values())
    dict_3["pontuação"] = total_ch

    for vl in dict_5.keys():
        total_ch = sum(dict_5.values())
    dict_5["pontuação"] = total_ch

    for vl in dict_7.keys():
        total_ch = sum(dict_7.values())
    dict_7["pontuação"] = total_ch

    #nova lista para pegar a pontuação
    lista_pontuacao = []
    #inserindo o primeiro elemento
    lista_pontuacao.insert(0,dict_1["pontuação"])
    lista_pontuacao.insert(1,dict_3["pontuação"])
    lista_pontuacao.insert(2,dict_5["pontuação"])
    lista_pontuacao.insert(3,dict_7["pontuação"])

    #somando valores na lista
    sum_list = sum(lista_pontuacao)
    return sum_list

