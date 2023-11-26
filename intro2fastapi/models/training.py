from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

def load_data():
    california_housing = fetch_california_housing()
    X, y = california_housing.data, california_housing.target
    return X, y

def preprocess_data(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, model_filename='intro2fastapi/models/california_trained_model.pkl'):
    joblib.dump(model, model_filename)

def main():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_train_processed = preprocess_data(X_train)
    model = train_model(X_train_processed, y_train)
    
    save_model(model)

if __name__ == "__main__":
    main()
