import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import httpx

# fast api applications 
app = FastAPI()

class InputData(BaseModel):
    features: list[float]


@app.post("/predict")
def predict(data:InputData):
    X = np.array(data.features)

    
    print(X)
    print(X.shape)
      #  Always return JSON-compatible data: dict, list, str, int, float, bool, or a Pydantic model.

    
    return {'features':f'{X}',
            'Shape':f'{X.shape}',
            'Predicted':'Class _1'
            }





"""other web services"""

@app.get("/srvc/")
def microservice(url:str):
  url = url.strip('"')
  response = httpx.get(url)
  
  return {'response': response.text}

