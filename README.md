# 🚀 Personal Assistant API

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A robust, production-ready RESTful API designed for a personal assistant application. This project integrates Finance Tracking, Event Management, and a unified Dashboard into a single scalable system.

Built with a focus on **Clean Architecture**, **Security**, and **Scalability**.

---

## 🌟 Key Features

### 🔐 Authentication & Users
* **JWT Authentication:** Secure access using `SimpleJWT` (Access & Refresh tokens).
* **Data Isolation:** Strict row-level security ensuring users can only access their own data.
* **Profile Management:** Secure user registration and profile retrieval.

### 💸 Finance Module
* **Decimal Precision:** Utilizes `DecimalField` for accurate monetary calculations (no floating-point errors).
* **Advanced Reporting:** Server-side aggregation using SQL `SUM` for instant balance calculation via the `/stats/` endpoint.
* **Filtering & Search:** Powerful filtering by date, transaction type (Income/Expense), and text search capabilities.
* **Categories:** Custom user-defined categories for better organization.

### 📅 Events & Calendar
* **Timezone Awareness:** Fully timezone-aware architecture ensuring correct scheduling across regions.
* **Smart Validation:** Custom logic (`clean` method) prevents invalid states, such as an end time occurring before a start time.
* **Computed Properties:** Dynamic fields (e.g., `is_passed`) calculated on-the-fly without database redundancy.

### 📊 Unified Dashboard
* **Aggregated Data:** A dedicated endpoint that compiles data from the Finance and Event modules into a single JSON response, optimizing frontend performance and reducing HTTP requests.

---

## 🛠 Tech Stack

* **Language:** Python 3.12
* **Framework:** Django 5.2
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** PostgreSQL 15
* **Containerization:** Docker & Docker Compose
* **Utilities:**
    * `django-filter` for advanced query filtering.
    * `python-decouple` for environment variable management.
    * `psycopg2-binary` for PostgreSQL connection.

---

## 🚀 Getting Started

This project is fully Dockerized for easy deployment and development.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/personal-assistant-api.git](https://github.com/YOUR_USERNAME/personal-assistant-api.git)
cd personal-assistant-api]
```

### 2. Environment Configuration
Create a .env file in the root directory. You can copy the following template:
```bash
# Django Settings
SECRET_KEY=your_super_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0

# Database Settings (PostgreSQL)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nexus_db
DB_USER=nexus_user
DB_PASSWORD=super_secret_password
DB_HOST=db
DB_PORT=5432
```
### 3. Run with Docker
Build and start the containers:
```bash
docker-compose up --build
```

### 4. Apply Migrations
Since this is a fresh database instance, you need to apply migrations and create a superuser:
```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Create a superuser (for Admin Panel access)
docker-compose exec web python manage.py createsuperuser
```
The API will be available at http://localhost:8000/

## 📚 API Documentation
### Auth
* **POST /api/users/register/** - Register a new user.
* **POST /api/token/** - Login (Obtain Access & Refresh tokens).
* **POST /api/token/refresh/** - Refresh an expired access token.
* **GET /api/users/me/** - Get current user profile.

### Finance
* **GET /api/finance/transactions/** - List transactions (Supports ?search=, ?ordering=, ?type=).
* **POST /api/finance/transactions/** - Create a transaction.
* **GET /api/finance/categories/** - Manage categories.
* **GET /api/finance/stats/** - Get total income, expenses, and balance.

### Events
* **GET /api/events/** - List upcoming events.
* **POST /api/events/** - Create a new event.

### Dashboard
* **GET /api/dashboard/** - Get a summary of finances and the next upcoming event.


## 📬 Contact
Arkadii Kyrylov Python Backend Developer [Email](mailto:arkadiykirilov@gmail.com) | [LinkedIn](https://www.linkedin.com/in/arkadii-kyrylov-04a5902bb/)