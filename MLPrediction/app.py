from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load Iris dataset to get class names
iris = load_iris()
class_names = iris.target_names  # ['setosa', 'versicolor', 'virginica']

# Initialize FastAPI app
app = FastAPI()

# Define input schema
class ModelInput(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict(input_data: ModelInput):
    try:
        # Convert input to numpy array
        input_array = np.array(input_data.features).reshape(1, -1)

        # Get prediction (integer label)
        prediction = model.predict(input_array)[0]

        # Map integer label to class name
        class_name = class_names[prediction]

        return {"prediction": class_name}
    except Exception as e:
        return {"error": str(e)}
