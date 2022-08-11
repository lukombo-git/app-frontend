import requests
from typer import params
from .import CURRICULUMS_API_URL

class CurriculumClient:
    @staticmethod
    def get_curriculums():
        response = requests.get(CURRICULUMS_API_URL+'/api/curriculums/all')
        return response.json()

    @staticmethod
    def count_curriculums():
        response = requests.get(CURRICULUMS_API_URL+'/api/curriculums/count_curriculums')
        return response.json()


    @staticmethod
    def get_curr_id(id_curriculum):
        id_curriculum = str(id_curriculum)
        response = requests.get(CURRICULUMS_API_URL +"/api/curriculums/"+ id_curriculum)
        return response.json()

    @staticmethod
    def delete_curr_id(id_curriculum):
        response = requests.delete(CURRICULUMS_API_URL+'/api/curriculums/delete/'+id_curriculum)
        return response.json()

    @staticmethod
    def create_curriculum(form):
        curriculum= None
        url = CURRICULUMS_API_URL +'/api/curriculums/create'
        response = requests.request("POST", url=url, data=form)
        if response:
            curriculum = response.json()
        return curriculum

    @staticmethod
    def update_curriculum(form,id_curriculum):
        curriculum = None
        url = CURRICULUMS_API_URL +"/api/curriculums/update_curr/"+id_curriculum
        response = requests.request("PUT", url=url, data=form)
        if response:
            curriculum = response.json()
        return curriculum
   
