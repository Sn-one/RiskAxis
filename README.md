# RiskAxis

RiskAxis is an objective-centered Enterprise Risk Management web application built with Django. It connects objectives, risks, controls, policies, assessments, appetite, treatments, indicators, incidents, reviews, assurance activities, dashboards, and reports.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in. Use `/admin/` to maintain reference data and ERM records.

## Docker

```bash
cp .env.example .env
docker compose up --build
```

## Documentation

Project documentation has been grouped in the [`docs/`](docs/) folder, including the PRD, TRD, UI/UX brief, application flow, schema notes, and references.

## Environment

See `.env.example` for the required runtime settings. Production should set a strong `SECRET_KEY`, `DEBUG=False`, PostgreSQL `DATABASE_URL`, secure host names, and trusted CSRF origins.
