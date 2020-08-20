from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.base import numpy as np

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data['H_AULA_PRES']= np.log1p(data['H_AULA_PRES'])                                                                          
        data['TAREFAS_ONLINE']= np.log1p(data['TAREFAS_ONLINE'])                                      
        data['FALTAS']= np.log1p(data['FALTAS'])
        data['INGLES']= np.log1p(data['INGLES'])
        data['NOTA_DE']= np.log1p(data['NOTA_DE'])
        data['NOTA_EM']= np.log1p(data['NOTA_EM']) 
        data['NOTA_MF']= np.log1p(data['NOTA_MF'])                                                                  
        data['NOTA_GO']= np.log1p(data['NOTA_GO']) 
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
 
