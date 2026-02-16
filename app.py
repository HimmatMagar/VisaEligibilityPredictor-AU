import pandas as pd
from fastapi import FastAPI
from typing import Annotated
from pydantic import Field, BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.visaPrediction.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # In production, specify your domain
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

class UserInput(BaseModel):
      age: Annotated[int, Field(..., description=("Enter your age: "))]
      gender: Annotated[str, Field(..., description=("Enter your Gender type: "))]
      visa_type: Annotated[str, Field(..., description=("Enter your visa type: "))]
      documents_submitted: Annotated[str, Field(..., description=("Enter your all documents you submitted: "))]


@app.get('/')
def home():
      return "hello"

predicts = PredictionPipeline()

@app.post("/predict")
def prediction(input: UserInput):
      data = pd.DataFrame([{
            'age': input.age,
            'gender': input.gender,
            'visa_type': input.visa_type,
            'documents_submitted': input.documents_submitted
      }])

      x = predicts.transform_user_input(data)
      pred = predicts.prediction(data=x)
      return {
            "prediction": pred.tolist() if hasattr(pred, 'tolist') else pred,
            "status": "success"
      } 
