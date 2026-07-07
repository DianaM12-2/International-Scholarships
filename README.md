# International Student Scholarship Finder 🌎

A full-stack web application that helps **international students** (F-1, OPT, J-1) discover and filter scholarship opportunities available to them in the United States.

Built with **React** (frontend) and **Python/Flask** (backend REST API).

---

## Why I Built This

As an international CS student on F-1 OPT, finding scholarships that actually accept international students is time-consuming and frustrating. Most scholarship databases don't filter by visa status. This project solves that — every scholarship listed has been verified for international student eligibility.

---

## Features

- 15 real scholarships for international/OPT/F-1/J-1 students
- Filter by degree level, visa status, and field of study
- Full-text search across name, provider, and description
- Stats dashboard (total, OPT-friendly, F-1 eligible, renewable)
- Scholarship detail modal with apply link
- REST API with 6 endpoints
- 11 pytest backend tests
- Docker Compose for one-command startup
- GitHub Actions CI (backend tests + frontend build)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, CSS |
| Backend | Python 3.12, Flask 3 |
| API | RESTful JSON |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions |

---

## Getting Started

### One command with Docker
```bash
git clone https://github.com/DianaM12-2/intl-scholarships.git
cd intl-scholarships
docker-compose up
```
- Frontend: `http://localhost:3000`
- API: `http://localhost:5000`

### Run separately

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python run.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Run backend tests
```bash
cd backend
pytest tests/ -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/scholarships` | Get all (supports `?degree=`, `?visa=`, `?field=`, `?search=`) |
| GET | `/api/v1/scholarships/<id>` | Get single scholarship |
| GET | `/api/v1/scholarships/stats` | Summary statistics |
| GET | `/api/v1/scholarships/fields` | All fields of study |
| GET | `/api/v1/scholarships/visa-types` | All visa types |
| GET | `/health` | Health check |

### Filter example
```bash
# Find OPT-friendly graduate CS scholarships
curl "http://localhost:5000/api/v1/scholarships?visa=F-1%20OPT&degree=graduate&field=Computer%20Science"
```

---

## Scholarships Included

Includes opportunities from: Google, Microsoft, Hispanic Scholarship Fund, Society of Women Engineers, Fulbright, AAUW, QuestBridge, OPTnation, GEM Consortium, NSF, AFCEA, Point Foundation, Palantir, Immigrants Rising, and more.

---

## Author

**Diana Martinez** — CS Graduate (Magna Cum Laude), University of the District of Columbia
International student on F-1 OPT — building tools to help others navigate the same journey.

[GitHub](https://github.com/DianaM12-2) · [LinkedIn](https://linkedin.com/in/diana-martinez-s) · [Portfolio](https://dianam12-2.github.io)
