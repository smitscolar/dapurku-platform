# DapurKu MVP

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python -m src.app

# Or with uvicorn
uvicorn src.app:app --reload
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user

### Sellers
- `POST /api/v1/sellers/` - Create seller profile
- `GET /api/v1/sellers/` - List sellers
- `GET /api/v1/sellers/{id}` - Get seller detail
- `PUT /api/v1/sellers/{id}/verify` - Verify seller

### Health
- `GET /api/v1/health` - Health check
- `GET /api/v1/ready` - Readiness check

## Testing

```bash
pytest tests/
```

## Tech Stack
- FastAPI + Python 3.11
- SQLAlchemy + SQLite (MVP)
- JWT Authentication
- Pydantic Validation
