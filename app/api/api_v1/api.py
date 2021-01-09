from fastapi import APIRouter

from .endpoints import predictor

router = APIRouter()
router.include_router(predictor.router, prefix="/predict", tags=["Predict"])