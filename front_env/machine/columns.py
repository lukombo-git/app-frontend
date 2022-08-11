
from front_env.machine.algoritmo_machine_learning import ReturnCandidatesIds
from front_env.machine.constantes import *
from front_env.machine.df_variaveis import *
from front_env.api.candidate_client import CandidateClient
import pandas as pd


def ConfigurationColumns():
    fields = CandidateClient.get_candidates()
    columns = []
    for column in fields.keys():
        if column == 'result':
            for ln in fields[column]:
                columns = list(ln.keys())
    if "id_candidato" in columns or "curriculum" in columns:
        columns.remove('id_candidato')
        columns.remove('curriculum')
    return columns