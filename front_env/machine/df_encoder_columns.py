from sklearn import preprocessing
import pandas as pd
from .df_variaveis import *
 
def ReturnEncoderColumns():
    #dataframe com as colunas a serem codificadas
    df_encoder_columns = DF_Variaveis()
    #TRANSFORMAÇAO DAS COLUNAS DO DATAFRAME
    labelEnconder = preprocessing.LabelEncoder()
   
    df_encoder_columns["nome_completo"] = labelEnconder.fit_transform(df_encoder_columns["nome_completo"])
  
    df_encoder_columns["habilitacoes_academica"] = labelEnconder.fit_transform(df_encoder_columns["habilitacoes_academica"])
  
    df_encoder_columns["grau"] = labelEnconder.fit_transform(df_encoder_columns["grau"])

    df_encoder_columns["instituicao"] = labelEnconder.fit_transform(df_encoder_columns["instituicao"])
 
    df_encoder_columns["curso"] = labelEnconder.fit_transform(df_encoder_columns["curso"])
    
    df_encoder_columns["provincia_residencia"] = labelEnconder.fit_transform(df_encoder_columns["provincia_residencia"])
    
    df_encoder_columns["area_candidatura"] = labelEnconder.fit_transform(df_encoder_columns["area_candidatura"])
   
    df_encoder_columns["disponibilidade"] = labelEnconder.fit_transform(df_encoder_columns["disponibilidade"])
  
    df_encoder_columns["nivel_ingles"] = labelEnconder.fit_transform(df_encoder_columns["nivel_ingles"])
    
    df_encoder_columns["curriculum"] = labelEnconder.fit_transform(df_encoder_columns["curriculum"])
    
    return df_encoder_columns