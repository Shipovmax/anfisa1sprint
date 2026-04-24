# Anfisa for Friends

A Django learning project from Yandex Backend Developer Course, Sprint 1 — three-app site with a homepage, about page, and ice cream catalog.

---

## Apps

- **homepage** — landing page (`/`)
- **about** — project description page (`/about/`)
- **ice_cream** — catalog list (`/ice-cream/`) and detail pages (`/ice-cream/<id>/`); data stored as a hardcoded Python list (no DB)

---

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Framework | Django 3.2 |
| Frontend | Bootstrap 4 (bundled) |
| Database | SQLite3 (default, unused) |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/anfisa1sprint
cd anfisa1sprint

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cd anfisa_for_friends
python manage.py migrate
python manage.py runserver
```

Site at `http://127.0.0.1:8000/`

---

## Project Structure

```
anfisa1sprint/
├── anfisa_for_friends/     # Django project root
│   ├── homepage/           # Landing page
│   ├── about/              # About page
│   ├── ice_cream/          # Catalog (list + detail views)
│   ├── templates/          # HTML templates per app
│   └── static_dev/         # CSS, images
├── html_templates/         # Original static HTML mockups
└── requirements.txt
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
