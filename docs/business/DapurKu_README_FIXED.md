# DapurKu - Ghost Kitchen UMKM Platform

[![CI/CD](https://github.com/[USERNAME]/dapurku-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/[USERNAME]/dapurku-platform/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🍳 About

DapurKu is Indonesia's ghost kitchen platform dedicated to UMKM food
entrepreneurs. We empower home cooks to sell their food online
without capital investment.

**Status**: Seed Stage (MVP Development)
**Founded**: 2025
**Pilot**: Batam, 2026

## 🚀 Features

- **Zero Capital**: Start selling with just your home kitchen
- **Low Commission**: 10-15% vs industry standard 20-30%
- **Community Support**: Training, packaging, marketing assistance
- **Pre-order System**: Cook-to-order, zero waste
- **Verified Kitchen**: Build buyer trust with certification

## 📊 Market

- **TAM**: Rp 100 trillion (Indonesia food delivery market 2026)
- **SAM**: Rp 20 trillion (UMKM food delivery segment)
- **SOM**: Rp 500 billion (0.5% penetrasi 5 tahun)
- **Target**: 60,000 sellers, 25 cities by 2030

## 🛠️ Tech Stack (CONSISTENT)

| Layer | Technology | Status |
|-------|-----------|--------|
| **Mobile** | Flutter (iOS & Android) | In Development |
| **Backend** | FastAPI, Python 3.11 | In Development |
| **Database** | PostgreSQL 15 | Planned |
| **Cache** | Redis 7 | Planned |
| **ML** | scikit-learn | Phase 2 |
| **Cloud** | AWS (ECS, RDS, S3) | Planned |
| **Payment** | Midtrans (primary), Xendit (backup) | In Development |
| **DevOps** | Docker, GitHub Actions | In Development |
| **Monitoring** | Sentry, Datadog | Planned |

**Note**: Tech stack konsisten di SEMUA dokumen (FastAPI, bukan Node.js).

## 🏁 Quick Start (Local Development)

```bash
# Clone repository
git clone https://github.com/[USERNAME]/dapurku-platform.git
cd dapurku-platform

# Setup environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your credentials

# Run locally
uvicorn src.app:app --reload
```

## 🐳 Docker (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access API at: http://localhost:8000
# API docs at: http://localhost:8000/docs
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html

# Run specific test
pytest tests/unit/test_sellers.py -v
```

## 📚 Documentation

- [API Documentation](docs/api.md) - OpenAPI/Swagger
- [Architecture](docs/architecture.md) - System design
- [Deployment](docs/deployment.md) - AWS deployment guide
- [Financial Model](docs/financial_model.md) - 5-year projections

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👥 Team

| Role | Name | LinkedIn | Background |
|------|------|----------|------------|
| CEO | [NAMA AKTUAL] | [LinkedIn] | 3 tahun GoFood (Ops) |
| CTO | [NAMA AKTUAL] | [LinkedIn] | 4 tahun Tokopedia (Engineer) |
| COO | [NAMA AKTUAL] | [LinkedIn] | 5 tahun Kemenkop UKM |
| CMO | [NAMA AKTUAL] | [LinkedIn] | 3 tahun Unilever (Brand) |

## 📞 Contact

- Website: [dapurku.id](https://dapurku.id)
- Email: hello@dapurku.id
- Instagram: [@dapurku](https://instagram.com/dapurku)
- TikTok: [@dapurku](https://tiktok.com/@dapurku)
- LinkedIn: [linkedin.com/company/dapurku](https://linkedin.com/company/dapurku)

---

Made with ❤️ in Indonesia

## 🔄 Changelog

### v0.1.0 (2026-06)
- Initial MVP setup
- FastAPI backend scaffold
- Flutter mobile scaffold
- Docker Compose setup
- CI/CD pipeline (GitHub Actions)

### Roadmap
- v0.2.0: Payment integration (Midtrans)
- v0.3.0: Seller onboarding flow
- v0.4.0: Order management system
- v0.5.0: Delivery partner integration
- v1.0.0: Public launch (Batam)
