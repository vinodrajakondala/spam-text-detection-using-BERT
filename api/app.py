from fastapi import FastAPI
import uvicorn
import numpy as np
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("../saved_models/beta/")
#prod_model=tf.keras.models.load_model("saved_models/1")
#beta_model=tf.keras.models.load_model("saved_models/2")

from typing import Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import tensorflow as tf 

app=FastAPI()
@app.get("/")
async def start():
  return {"Hello World"}

MODEL = tf.keras.models.load_model("saved_models/1")
#prod_model=tf.keras.models.load_model("saved_models/1")
#beta_model=tf.keras.models.load_model("saved_models/2")

CLASS_NAMES = ["spam","ham"]


# @app.get("/intro")
# async def Intro():
#     return "Hello World!"


@app.post("/predict")
async def predict(q: Optional[str] = None):
    review = [q]
    if q is None:
      return {"Please enter text body to check SPAM or HAM"}

    else:
      predictions = MODEL.predict(review)
      pred = predictions.flatten()

      if pred > 0.5:
        return {" It's a SPAM mail"}
      else:
        return {" It's a Ham mail "}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)