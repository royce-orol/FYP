# ===============================
# Cell 1: Handling Missing Values
# ===============================
import pandas as pd
import numpy as np

def handle_missing_values(df, strategy='mean', fill_value=None):
    """
    Handles missing values in a DataFrame.
    strategy: 'mean', 'median', 'mode', or 'constant'
    fill_value: value to use if strategy is 'constant'
    """
    df_cleaned = df.copy()
    for col in df_cleaned.columns:
        if df_cleaned[col].isnull().sum() > 0:
            if strategy == 'mean' and df_cleaned[col].dtype in [np.float64, np.int64]:
                df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            elif strategy == 'median' and df_cleaned[col].dtype in [np.float64, np.int64]:
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
            elif strategy == 'mode':
                df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
            elif strategy == 'constant':
                df_cleaned[col].fillna(fill_value, inplace=True)
    return df_cleaned

# ===============================
# Cell 2: Handling Inconsistent Data
# ===============================
def handle_inconsistent_data(df, column, valid_values):
    """
    Replaces values not in valid_values with np.nan in the specified column.
    """
    df_cleaned = df.copy()
    df_cleaned[column] = df_cleaned[column].apply(lambda x: x if x in valid_values else np.nan)
    return df_cleaned

# ===============================
# Cell 3: Encoding Categorical Variables
# ===============================
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def encode_categorical(df, columns, encoding_type='onehot'):
    """
    Encodes categorical columns using label or one-hot encoding.
    encoding_type: 'label' or 'onehot'
    """
    df_encoded = df.copy()
    if encoding_type == 'label':
        le = LabelEncoder()
        for col in columns:
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    elif encoding_type == 'onehot':
        df_encoded = pd.get_dummies(df_encoded, columns=columns)
    return df_encoded

# ===============================
# Cell 4: Handling Class Imbalance
# ===============================
from imblearn.over_sampling import SMOTE

def handle_class_imbalance(X, y):
    """
    Uses SMOTE to handle class imbalance.
    Returns resampled X, y.
    """
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)
    return X_res, y_res

# ===============================
# Cell 5: Train-Test Split
# ===============================
from sklearn.model_selection import train_test_split

def split_train_test(X, y, test_size=0.2, random_state=42):
    """
    Splits data into train and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# ===============================
# Cell 6: Feature Selection using Multivariate Chi-Square Test
# ===============================
from sklearn.feature_selection import SelectKBest, chi2

def chi_square_feature_selection(X, y, k=10):
    """
    Selects top k features using chi-square test.
    X must be non-negative (e.g., after encoding categorical variables).
    """
    selector = SelectKBest(score_func=chi2, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support(indices=True)]
    return X_new, selected_features

# ===============================
# Cell 7: Correlation Analysis
# ===============================
def correlation_analysis(df):
    """
    Returns the correlation matrix of the DataFrame.
    """
    corr_matrix = df.corr()
    return corr_matrix 