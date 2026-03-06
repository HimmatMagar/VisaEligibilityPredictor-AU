from sklearn.base import BaseEstimator, TransformerMixin

class DataCleaner(BaseEstimator, TransformerMixin):
    """
    Custom transformer to clean the visa data.
    """
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        if 'rejection_reason' in df.columns:
            df.drop(columns='rejection_reason', inplace=True)
        if 'documents_submitted' in df.columns:
            df['documents_submitted'] = df['documents_submitted'].str.replace(',', ' ', regex=True).str.lower()
        return df