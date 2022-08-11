import requests
from .import VAGAS_API_URL

class VagasClient:

    @staticmethod
    def create_vagas(form):
        vaga= None
        payload = {
            'titulo_vaga':form.titulo_vaga.data,
            'categoria_vaga':form.categoria_vaga.data,
            'area_candidatura':form.area_candidatura.data,
            'descricao_vaga':form.descricao_vaga.data,
            'tipo_vaga':form.tipo_vaga.data,
            'requisitos_vaga':form.requisitos_vaga.data,
            'perfil_candidato':form.perfil_candidato.data,
            'habilitacoes':form.habilitacoes.data,
            'provincia_vaga':form.provincia_vaga.data,
            'nivel_ingles_vaga':form.nivel_ingles_vaga.data,
            'habilidades_exigida':form.habilidades_exigida.data,
            'experiencia_profissional':form.experiencia_profissional.data,
            'anos_exp_exigida':form.anos_exp_exigida.data,
            'data_inicio_vaga':form.data_inicio_vaga.data,
            'data_termino_vaga':form.data_termino_vaga.data
        }
        url = VAGAS_API_URL +'/api/vagas/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            vaga = response.json()
        return vaga

    @staticmethod
    def update_vagas(form,id_vaga):
        vagas = None
        url = VAGAS_API_URL +"/api/vagas/update_vaga_id/"+id_vaga
        response = requests.request("PUT", url=url, data=form)
        if response:
            vagas = response.json()
        return vagas

    @staticmethod
    def get_vagas():
        response = requests.get(VAGAS_API_URL+'/api/vagas/all')
        return response.json()

    @staticmethod
    def get_vaga_id(id_vaga):
        response = requests.get(VAGAS_API_URL+'/api/vagas/'+id_vaga)
        return response.json()

    @staticmethod
    def count_vagas():
        response = requests.get(VAGAS_API_URL+'/api/vagas/count_vagas')
        return response.json()

    @staticmethod
    def delete_vaga_id(id_vaga):
        response = requests.delete(VAGAS_API_URL+'/api/vagas/delete/'+id_vaga)
        return response.json()
    
