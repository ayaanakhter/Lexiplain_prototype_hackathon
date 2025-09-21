import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# --- 1. SET YOUR DATASET PATH HERE ---
# Example for Windows: dataset_path = r'C:\Users\YourUser\Downloads\IMDB-Dataset.csv'
# Example for Mac/Linux: dataset_path = '/home/youruser/downloads/IMDB-Dataset.csv'
dataset_path = r"C:\Users\ayaan\OneDrive\Documents\IMDB Dataset.csv"

# --- 2. LOAD AND PREPARE DATA ---
try:
    df = pd.read_csv(dataset_path)
    X = df['review']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- 3. TRAIN MODEL ---
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # --- 4. SAVE ARTIFACTS ---
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    print("Training complete. 'model.pkl' and 'vectorizer.pkl' created.")
    print(f"Model accuracy: {model.score(X_test_vec, y_test):.4f}")

except FileNotFoundError:
    print(f"Error: The file was not found at the path: {dataset_path}")
except Exception as e:
    print(f"An error occurred: {e}")