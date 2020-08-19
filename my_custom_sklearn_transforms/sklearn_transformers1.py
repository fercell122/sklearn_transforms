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
        return data.log1p(labels=self.colunas, axis='colunas')
