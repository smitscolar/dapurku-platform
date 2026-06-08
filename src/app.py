"""DapurKu Main Application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config import settings
from src.utils.database import init_db
from src.api import auth, sellers, buyers, orders, payments, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown
    pass

app = FastAPI(
    title=settings.APP_NAME,
    description="Ghost Kitchen UMKM Platform - MVP",
    version=settings.APP_VERSION,
    lifespan=lifespan
)

# CORS - Restricted
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(sellers.router, prefix="/api/v1/sellers")
app.include_router(buyers.router, prefix="/api/v1/buyers")
app.include_router(orders.router, prefix="/api/v1/orders")
app.include_router(payments.router, prefix="/api/v1/payments")

@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "operational",
        "endpoints": {
            "auth": "/api/v1/auth",
            "sellers": "/api/v1/sellers",
            "buyers": "/api/v1/buyers",
            "orders": "/api/v1/orders",
            "payments": "/api/v1/payments",
            "health": "/api/v1/health"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
