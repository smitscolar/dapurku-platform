# DapurKu - Ghost Kitchen UMKM Platform 🍳

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/smitscolar/dapurku-platform)
[![Status](https://img.shields.io/badge/status-Investor%20Ready-green.svg)](https://github.com/smitscolar/dapurku-platform)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## 🚀 Investor-Ready Package v2.0

**DapurKu** adalah platform ghost kitchen untuk UMKM makanan rumahan di Indonesia. Kami membantu 15 juta ibu rumah tangga yang bisa memasak untuk menjadi entrepreneur makanan.

---

## 📦 Package Contents

### 📄 Business Documents (Revised)
| Document | Status | Description |
|----------|--------|-------------|
| [Term Sheet](DapurKu_Term_Sheet_FIXED.txt) | ✅ Revised | Cap table corrected, 20% ownership |
| [Financial Model](DapurKu_Financial_Model_FIXED.txt) | ✅ Balanced | GMV, revenue, balance sheet fixed |
| [Investor FAQ](DapurKu_Investor_FAQ_FIXED.txt) | ✅ Updated | Tech stack consistent, realistic metrics |
| [Pitch Deck](DapurKu_Pitch_Deck_FIXED.txt) | ✅ Revised | Market size realistic, risk disclosure |
| [Press Release](DapurKu_Press_Release_FIXED.txt) | ✅ Updated | Source citations added |
| [Email Templates](DapurKu_Email_Templates_FIXED.txt) | ✅ Professional | Less confrontational tone |
| [Video Script](DapurKu_Video_Script_FIXED.txt) | ✅ Revised | Timeline realistic |
| [Legal Checklist](DapurKu_Legal_Checklist_FIXED.txt) | ✅ Compliant | UU PDP/PSE/halal BEFORE LAUNCH |
| [Hiring Plan](DapurKu_Hiring_Plan_FIXED.txt) | ✅ Realistic | Salary seed stage, headcount fixed |

### 📊 Data & Analytics
| File | Description |
|------|-------------|
| [Complete Data](DapurKu_COMPLETE_DATA_FIXED.xlsx) | 38 provinces, 0.5% penetration |
| [Target Market](GhostKitchen_Target_Pasar_38_Provinsi_FIXED.xlsx) | 5-year projection |
| [Gantt Chart](DapurKu_Gantt_Chart_5_Year_FIXED.png) | Realistic timeline |
| [Dashboard](DapurKu_Dashboard_Pilot.png) | Pilot data mockup |
| [Architecture](DapurKu_Architecture_Diagram.png) | System design |
| [Social Media](DapurKu_Social_Media_Calendar_30_Days_FIXED.xlsx) | 30-day content calendar |

### 💻 MVP Code
| Component | Tech Stack |
|-----------|-----------|
| Backend | FastAPI + Python 3.11 |
| Mobile | Flutter (iOS & Android) |
| Database | PostgreSQL 15 + Redis 7 |
| Payment | Midtrans + Xendit |
| Cloud | AWS (ECS, RDS, S3) |
| DevOps | Docker + GitHub Actions |

**API Endpoints:**
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/sellers/` - Create seller
- `GET /api/v1/sellers/` - List sellers
- `POST /api/v1/orders/` - Create order
- `POST /api/v1/payments/` - Process payment
- `GET /api/v1/health` - Health check

---

## 📊 Key Metrics

| Metric | Value |
|--------|-------|
| **Seed Round** | Rp 500 juta for 20% |
| **Pre-money Valuation** | Rp 2 miliar |
| **Post-money Valuation** | Rp 2.5 miliar |
| **TAM** | Rp 100 triliun (food delivery) |
| **SAM** | Rp 20 triliun (UMKM segment) |
| **SOM** | Rp 500 miliar (0.5% penetration) |
| **Pilot (Batam)** | 50 sellers, 524 transactions, 4.7/5 rating |
| **Break-even** | Month 8-10 (Batam) |
| **5-Year Target** | 60,000 sellers, 25 cities, Rp 5T GMV |

---

## 👥 Team

| Role | Name | Background | LinkedIn |
|------|------|------------|----------|
| CEO | [Your Name] | 3 years GoFood (Ops) | [linkedin.com/in/...] |
| CTO | [Your Name] | 4 years Tokopedia (Engineer) | [linkedin.com/in/...] |
| COO | [Your Name] | 5 years Kemenkop UKM | [linkedin.com/in/...] |
| CMO | [Your Name] | 3 years Unilever (Brand) | [linkedin.com/in/...] |

**Advisors:**
- Ex-CEO GoFood (Strategic)
- Ex-Minister Kemenkop (Government Relations)

---

## 🛠️ Tech Stack (Consistent)

```
Mobile:     Flutter (iOS + Android)
Backend:    FastAPI + Python 3.11
Database:   PostgreSQL 15 + Redis 7
ML:         scikit-learn (Phase 2)
Cloud:      AWS (ECS, RDS, S3, CloudFront)
Payment:    Midtrans (primary) + Xendit (backup)
DevOps:     Docker + GitHub Actions v4
Monitoring: Sentry + Datadog
```

---

## 🏁 Quick Start (Local Development)

```bash
# Clone repository
git clone https://github.com/smitscolar/dapurku-platform.git
cd dapurku-platform

# Extract MVP code
cd dapurku-mvp

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m src.app

# Or with uvicorn
uvicorn src.app:app --reload
```

Access API at: `http://localhost:8000`
API Docs at: `http://localhost:8000/docs`

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html
```

---

## 📞 Contact

- **Website:** [dapurku.id](https://dapurku.id)
- **Email:** hello@dapurku.id
- **Instagram:** [@dapurku](https://instagram.com/dapurku)
- **TikTok:** [@dapurku](https://tiktok.com/@dapurku)
- **LinkedIn:** [linkedin.com/company/dapurku](https://linkedin.com/company/dapurku)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔄 Changelog

### v2.0 (2026-06) - Investor Ready
- ✅ 80+ issues fixed across all documents
- ✅ Financial model balanced and realistic
- ✅ Tech stack consistent (FastAPI)
- ✅ Legal compliance timeline updated
- ✅ MVP code with 5 API endpoints
- ✅ Website landing page included
- ✅ Dashboard mockup for pilot data

### v1.0 (2026-06) - Initial Upload
- Initial package with basic documents

---

**Made with ❤️ in Indonesia**

*Last updated: June 8, 2026*
