# Challenge Week — EPITA International Programs (2025f)

Intensive development week. Mixed **SE + CS** teams work on the same bootstrap projects:
- **SE students** build features (API endpoints + mobile app)
- **CS students** audit, exploit, and harden

**Duration:** 5 days (Monday–Friday)
**Teams:** 3–4 students (2 SE + 1–2 CS)
**Stack:** Python (Flask/FastAPI) + MySQL + Android (Java) or iOS (Swift)

---

## Projects

| # | Project | Folder | Backend | Theme |
|---|---------|--------|---------|-------|
| 1 | Campus Event Planner | [01-campus-event-planner](01-campus-event-planner/) | Flask + MySQL | Campus events, registration |
| 2 | Student Marketplace | [02-student-marketplace](02-student-marketplace/) | FastAPI + MySQL | Student classifieds |
| 3 | Fitness Tracker | [03-fitness-tracker](03-fitness-tracker/) | Flask + MySQL | Workout tracking |
| 4 | Study Flashcards | [04-study-flashcards](04-study-flashcards/) | FastAPI + MySQL | Revision cards |
| 5 | Campus Food Guide | [05-campus-food-guide](05-campus-food-guide/) | Flask + MySQL | Restaurant ratings |

Each project is ~60% complete with a working backend, seeded database, and basic mobile app.

---

## Getting Started

```bash
# Pick a project
cd 01-campus-event-planner/backend

# Set up Python environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Seed the database (MySQL must be running)
python seed.py

# Run the API
python app.py
```

Then open the Android project in Android Studio or the iOS project in Xcode.

See each project's README for detailed instructions.

---

## Repository Structure

```
├── 01-campus-event-planner/
│   ├── backend/        # Flask API + MySQL
│   ├── android/        # Android (Java)
│   └── ios/            # iOS (Swift)
├── 02-student-marketplace/
│   ├── backend/        # FastAPI + MySQL
│   ├── android/
│   └── ios/
├── 03-fitness-tracker/
│   └── ...
├── 04-study-flashcards/
│   └── ...
└── 05-campus-food-guide/
    └── ...
```

---

## SE Track — 40 TODOs per project

TODOs are marked in the code with `// TODO PROJ-S###` or `# TODO PROJ-S###`.
They cover API endpoints, mobile UI, data validation, and integration.

## CS Track — 30 TODOs per project

| Pillar | Tags | TODOs |
|--------|------|-------|
| Threat Modeling | `[Threat]` | C001–C006 |
| Code Review / Bug Bounty | `[Review]` | C007–C016 |
| Security Testing | `[Test]` | C017–C024 |
| Deployment & Hardening | `[Deploy]` | C025–C030 |

---

## Grading

- **SE:** continuous assessment (daily checkpoints) + final presentation
- **CS:** continuous assessment (daily checkpoints) + final audit report + presentation
- **Collaboration bonus:** joint hardening session (Thursday) + joint presentation (Friday)
