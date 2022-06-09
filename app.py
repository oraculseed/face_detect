# Imports
from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from pydantic import BaseModel
import numpy as np
import sys

import cv2
import base64
import io

def detect_face(image): 
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))   
    net.setInput(blob)
    detections = net.forward()    
    face = False    
    for i in range(0, detections.shape[2]):
      confidence = detections[0, 0, i, 2]
      if confidence > 0.5:
        face = True   
    return face


app = FastAPI()

print("[INFO] loading model...")
prototxt = 'deploy.prototxt'
model = 'res10_300x300_ssd_iter_140000.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt, model)


class Content(BaseModel):
    content: str
class Prediction(BaseModel):
    face: bool


@app.get('/')
def root_route():
    return { 'error': 'Error route!' }

@app.post('/prediction/', response_model=Prediction)
async def prediction_route(content: Content):

    try:
        
        img_content = str(content).split("content=")[1].replace("'","")        
        image = base64.b64decode(img_content)
        image = np.frombuffer(image, np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        face = detect_face(image)
        
        return {'face':face}

    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
        return {'face':False}
