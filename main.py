from fastapi import FastAPI
from transformers import pipeline

class Item(BaseModel):
    text: str
app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    return {"message": "Hello UrFU"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
    
   
