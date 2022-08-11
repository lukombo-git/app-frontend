from front_env.api.candidate_client import *
import pandas as pd

def DF_Variaveis():
    fields = CandidateClient.get_candidates()
    columns = []
    for column in fields.keys():
        if column == 'result':
            for ln in fields[column]:
                columns = list(ln.keys())
    #Creating the dataframe
    dataframe = pd.DataFrame([value for value in fields['result']])
    dataframe.columns = columns
    
    return dataframe


