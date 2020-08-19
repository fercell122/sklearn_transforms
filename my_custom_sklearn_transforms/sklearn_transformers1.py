from sklearn.base import BaseEstimator, TransformerMixin

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
