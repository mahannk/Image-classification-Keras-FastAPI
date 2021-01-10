from fastapi import APIRouter, status, Response
from fastapi import UploadFile, File
from ....dependencies.model import Prediction
import numpy as np

router = APIRouter()
predictor = Prediction() 

@router.post("/")
async def predict(reponse: Response, image: UploadFile = File(...)):

    if image.content_type not in ('image/jpeg', 'image/jpg', 'image/png'):
        reponse.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        return {'message' : "File format not supported"}
    
    else:
        img = predictor.load_image(await image.read())
        results = predictor.predict(img)

        reponse.status_code = status.HTTP_202_ACCEPTED


    return {"message" : "success", "predictions" : results}