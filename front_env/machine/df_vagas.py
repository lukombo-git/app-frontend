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

def ReturnTitulo():
    i = 0
    lista_tokens = [] 
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):     
            tokens = word_tokenize(new_vagas["result"][i]["titulo_Vaga"])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

#função pra retornar a descrição da vaga
def ReturnDescricao():
    i = 0
    lista_tokens = []
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):     
            tokens = word_tokenize(new_vagas["result"][i]["descricao_vaga"])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

#funcao para retornar o tipo de vaga
def ReturnTipoVaga():
    #lista das areas
    tipo_vaga_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            tipo_vaga=new_vagas["result"][i]["tipo_vaga"]
            tipo_vaga_list.append(tipo_vaga)
            i+=1
    return tipo_vaga_list

#função para retornar a área de candidatura da vaga
def ReturnAreaVaga():
    #lista das areas
    area_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            area_vaga=new_vagas["result"][i]["area_candidatura"]
            area_list.append(area_vaga)
            i+=1
    return area_list

#função para retornar habilitacoes de candidatura da vaga
def ReturnHabilitacoes():
    #lista das areas
    hab_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            hab=new_vagas["result"][i]["habilitacoes"]
            hab_list.append(hab)
            i+=1
    return hab_list

#função para retornar habilitacoes de candidatura da vaga
def ReturnProvincia():
    #lista das areas
    prov_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            prov=new_vagas["result"][i]["provincia_vaga"]
            prov_list.append(prov)
            i+=1
    return prov_list

#função para retornar habilitacoes de candidatura da vaga
def ReturnNivelIngles():
    #lista das areas
    ingles_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            ingles=new_vagas["result"][i]["nivel_ingles_vaga"]
            ingles_list.append(ingles)
            i+=1
    return ingles_list

#função para retornar habilitacoes de candidatura da vaga
def ReturnHabilidadesExigida():
    #lista das areas
    hab_exig_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            hab_exig=new_vagas["result"][i]["habilidades_exigida"]
            hab_exig_list.append(hab_exig)
            i+=1
    return hab_exig_list

#função para retornar o ano de experiência necessitada na vaga
def ReturnAnoExperiencia():
    #lista das areas
    exp_list = []
    i = 0
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):
            exp=new_vagas["result"][i]["anos_exp_exigida"]
            exp_list.append(exp)
            i+=1
    return exp_list

#função para retornar a experiência necessitada na vaga
def ReturnExperienciaProfissional():
    i = 0
    lista_tokens = []
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):     
            tokens = word_tokenize(new_vagas["result"][i]["experiencia_profissional"])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

#funcao para retornar os requisitos
def ReturnRequisitos():
    i = 0
    lista_tokens = []
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):     
            tokens = word_tokenize(new_vagas["result"][i]["requisitos_vaga"])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

#função para retornar o perfil
def ReturnPerfil():
    i = 0
    lista_tokens = []
    for valor in new_vagas["result"]:
        while i < len(new_vagas["result"]):     
            tokens = word_tokenize(new_vagas["result"][i]["perfil_candidato"])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val