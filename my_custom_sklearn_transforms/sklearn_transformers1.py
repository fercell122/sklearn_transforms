from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
class transformisloga(BaseEstimator, TransformerMixin):
    def __init__(self, colunas):
        self.colunas = colunas

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe com log
       #return   np.log1p(data[self.columns]) + data['PERFIL']???
        data['H_AULA_PRES']= np.log1p(data['H_AULA_PRES'])                                                                          
        data['TAREFAS_ONLINE']= np.log1p(data['TAREFAS_ONLINE'])                                      
        data['FALTAS']= np.log1p(data['FALTAS'])
        data['NOTA_DE']= np.log1p(data['NOTA_DE'])
        data['NOTA_EM']= np.log1p(data['NOTA_EM']) 
        data['NOTA_MF']= np.log1p(data['NOTA_MF'])                                                                  
       

        return data
