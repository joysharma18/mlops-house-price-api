import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from pathlib import Path # Import the Path object

def train_model():
    """Trains a regression model and saves it to the correct directory."""
    # --- No changes here ---
    housing = fetch_california_housing()
    X, y = housing.data, housing.target
    model = LinearRegression()
    model.fit(X, y)
    print("✅ Model trained.")
    
    # --- This is the updated part ---
    # 1. Get the directory of the current script (app/)
    script_dir = Path(__file__).parent
    # 2. Define the path to save the model (go up one level to the root, then into model/)
    save_path = script_dir.parent / "model" / "house_price_model.pkl"

    # 3. Ensure the model directory exists
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 4. Save the model to the constructed path
    joblib.dump(model, save_path)
    print(f"✅ Model saved to {save_path}")

if __name__ == '__main__':
    train_model()