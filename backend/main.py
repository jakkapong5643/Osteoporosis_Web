from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inputWeight = pd.read_csv('Data/inputWeightInference.csv', header=None).values
outputWeight = pd.read_csv('Data/outputWeightInference.csv', header=None).values
bias = pd.read_csv('Data/biasInference.csv', header=None).values

def maxtwoind_mammo(x):
    y = []
    for i in range(x.shape[0]):
        n = np.argmax(x[i, :])
        if n == 0:
            y.append([1, 0])
        elif n == 1:
            y.append([0, 1])
        else:
            print("error")
            break
    return np.array(y)

def maxtwoindclass_mammo(x):
    y = []
    for i in range(x.shape[0]):
        n = x[i, :]
        if np.array_equal(n, [1, 0]):
            x[i] = 1
        elif np.array_equal(n, [0, 1]):
            x[i] = 2
        else:
            print("Error")
            break
        y.append(x[i])
    return np.array(y)

class InputData(BaseModel):
    X_new: list

@app.post("/predict/")
async def predict(data: InputData):
    X_new = np.array(data.X_new)

    H_new = 1 / (1 + np.exp(-(X_new @ inputWeight + np.tile(bias, (X_new.shape[0], 1)))))
    outputNew = np.dot(H_new, outputWeight)
    yNew = maxtwoind_mammo(outputNew)
    predictionsNew = maxtwoindclass_mammo(yNew)
    predictionsNew = predictionsNew[1, 1]

    if predictionsNew == 2:
        result = "Yes Osteoporosis"
    elif predictionsNew == 1:
        result = "No Osteoporosis"
    else:
        result = "Error in Prediction"

    confidence = np.max(outputNew)

    return {"prediction": result, "confidence": confidence}