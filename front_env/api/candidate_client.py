import requests
from typer import params
from .import CANDIDATES_API_URL

class CandidateClient:
    @staticmethod
    def get_candidates():
        response = requests.get(CANDIDATES_API_URL+'/api/candidates/all')
        return response.json()

    @staticmethod
    def count_candidates():
        response = requests.get(CANDIDATES_API_URL+'/api/candidates/count_candidates')
        return response.json()

    @staticmethod
    def get_10_candidates():
        response = requests.get(CANDIDATES_API_URL+'/api/candidates/10_candidates')
        return response.json()

    @staticmethod
    def get_cand_id(id_candidate):
        id_candidato = str(id_candidate)
        print(type(id_candidato))
        response = requests.get(CANDIDATES_API_URL +"/api/candidates/"+ id_candidato)
        return response.json()

    @staticmethod
    def delete_cand_id(id_candidate):
        response = requests.delete(CANDIDATES_API_URL+'/api/candidates/delete/'+id_candidate)
        return response.json()

    @staticmethod
    def create_candidate(form):
        candidate= None
        url = CANDIDATES_API_URL +'/api/candidates/create'
        response = requests.request("POST", url=url, data=form)
        if response:
            candidate = response.json()
        return candidate

    @staticmethod
    def update_candidate(form,id_candidato):
        candidate = None
        url = CANDIDATES_API_URL +"/api/candidates/update_cand/"+id_candidato
        response = requests.request("PUT", url=url, data=form)
        if response:
            candidate = response.json()
        return candidate

    @staticmethod
    def get_cand_nome(nome_completo):
        response = requests.get(CANDIDATES_API_URL +"/api/candidates/"+ nome_completo)
        return response.json()
   
