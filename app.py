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
async def home():
      return "hello"

predicts = PredictionPipeline()

@app.post("/predict")
async def prediction(input: UserInput):
      # build a dataframe from user input so we can echo it back if needed
      data = pd.DataFrame([{
            'age': input.age,
            'gender': input.gender,
            'visa_type': input.visa_type,
            'documents_submitted': input.documents_submitted
      }])

      # run through pipeline
      pred = predicts.prediction(data=data)

      # normalize prediction into a list so we can work with it easily
      if hasattr(pred, 'tolist'):
            pred_list = pred.tolist()
      else:
            pred_list = [pred]

      # convert numeric/boolean output to human-readable Yes/No if appropriate
      def human_label(val):
            if isinstance(val, str):
                  return val
            try:
                  # assume binary 0/1
                  return "Yes" if int(val) == 1 else "No"
            except Exception:
                  return val

      readable = [human_label(p) for p in pred_list]

      # only return the human-readable prediction and a status
      result = {
            "prediction": readable,
            "status": "success"
      }

      return result 
