"""Health Check API"""
from fastapi import APIRouter
from datetime import datetime

from src.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": settings.APP_VERSION,
        "service": settings.APP_NAME
    }

@router.get("/ready")
async def readiness_check():
    # TODO: Check database connectivity
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat()
    }
