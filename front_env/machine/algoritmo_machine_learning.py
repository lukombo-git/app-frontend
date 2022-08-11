from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

from front_env.machine.df_variaveis import DF_Variaveis

#funcao decision tree
def KNeighborsModel(x_train,y_train):
    classifier = KNeighborsClassifier(n_neighbors=2)
    classifier.fit(x_train,y_train)
    return classifier

#função principal do algoritmo
def ClassifierFunction(x_train,x_test,y_train,y_test,classification_fn):
    model = classification_fn(x_train,y_train)
    y_pred = model.predict(x_test)
    train_score = model.score(x_train,y_train)
    test_score = accuracy_score(y_test,y_pred)
    #erro de previsão
    error_rate = mean_absolute_error(y_test, y_pred)
    #vector de matrix
    matrix_vector = confusion_matrix(y_test,y_pred)
    return y_pred

#função principal
def ReturnCandidatesIds(values_list):
#def ReturnCandidatesIds():
    #pegando o dataframe dos candidatos
    df_candidatos = DF_Variaveis()
    #copy do dataframe
    dataframe_copy = df_candidatos.copy()
    #codificando as colunas
    labelEnconder = preprocessing.LabelEncoder()
    #estamos a codificar cada linha
    for dt in df_candidatos:
        df_candidatos[dt] = labelEnconder.fit_transform(df_candidatos[dt])
    #INSERINDO VALORES NAS VARIÁVEIS PARA PREVISÃO
    X = df_candidatos.drop(['id_candidato'],axis=1)
    Y = dataframe_copy["id_candidato"]
    #aplicando o treino e teste
    x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.8,test_size=0.2,random_state=101)
    #imprimindo o resultado
    resultado = ClassifierFunction(x_train,x_test,y_train,y_test,KNeighborsModel)
    return resultado


