# Django_for_Professionals_by_William_Vincent

# Django for Professionals

A production-ready Django project built by following *Django for Professionals* by William S. Vincent.

## 🚀 Features

* Django 5.0
* PostgreSQL as the database
* Docker & Docker Compose for development and production environments
* Custom user model
* Static and media file handling with Whitenoise
* Environment variable management with `django-environ`
* Secure settings for production (allowed hosts, secret key, database, etc.)
* Gunicorn + Nginx setup for deployment

---

## 📦 Requirements

* [Python 3.11+](https://www.python.org/)
* [Docker & Docker Compose](https://docs.docker.com/)
* [PostgreSQL](https://www.postgresql.org/) (if running without Docker)

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/Clinton-odia/Django_for_Professionals_by_William_Vincent.git
cd Django_for_Professionals_by_William_Vincent
```

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

---

## 🐳 Running with Docker

Build and start containers:

```bash
docker-compose up -d --build
```

Run migrations:

```bash
docker-compose exec web python manage.py migrate
```

Create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

Collect static files:

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

Visit the app:

* Local: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧑‍💻 Running without Docker

Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and runserver:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🛠️ Development Workflow

* Run tests:

  ```bash
  docker-compose exec web python manage.py test
  ```
* Check code style (flake8, black, isort):

  ```bash
  black .
  isort .
  flake8
  ```

---

## 🚀 Deployment

For production deployment:

1. Update `.env` with secure values (`DEBUG=0`, `ALLOWED_HOSTS`, `DATABASE_URL`)
2. Build images:

   ```bash
   docker-compose -f docker-compose.prod.yml up -d --build
   ```
3. Use **Gunicorn** + **Nginx** for serving the app
4. Set up HTTPS with **Let’s Encrypt**

---

## 📚 Reference

* Book: [Django for Professionals](https://djangoforprofessionals.com/) by William S. Vincent
* Django Docs: [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
* Docker Docs: [https://docs.docker.com/](https://docs.docker.com/)

---
