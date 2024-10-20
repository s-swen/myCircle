# MyCircle 🎉
Organize and manage your personal relationship circles with ease. MyCircle is a backend project demonstrating my backend engineering skills using Django, PostgreSQL, containerization, and cloud deployment.

## 📚 Project Overview
MyCircle helps users organize contacts into relationship circles (e.g., professionals, friends, doctors) and store their contact details (emails, phone numbers, social media profiles). Users can set reminders for birthdays, anniversaries, and log the last time they reached out. This project showcases API design, SQL, ORM, authentication, encryption, CI/CD, testing, and cloud deployment.

---

## 🗄️ Database
- **Development**: SQLite
- **Production**: PostgreSQL
- **Tables**:
  - **Users**: Stores user details and authentication information.
  - **Contacts**: Stores information such as emails, phone numbers, social media profiles, and category (friends, professionals, etc.).
  - **Events**: Tracks birthdays, anniversaries, and other key dates.
  - **Logs**: Records the last contact date with each person for relationship tracking.
  
---

## 📡 API
- **Framework**: Django Rest Framework (DRF)
- **Endpoints**:
  - CRUD for users and contacts (GET, POST, PUT, DELETE)
  - Reminders management (GET upcoming reminders, POST to update contact status)
- **Usage**: Can be consumed via frontend, Postman, curl, or wget.

---

## 🛠️ SQL Proficiency
- Raw SQL for creating tables, managing indexes, and data manipulation.
- Leverage PostgreSQL features like indexing for performance optimization.
- Primarily use Django ORM, with strategic raw SQL queries where appropriate.

---

## 📁 File Output
- **Export Options**:
  - Export contacts as CSV, Excel, or PDF.
  - Use libraries such as `pandas` or `ReportLab` for generating reports.

---

## 🔒 Authentication & Security
- **Authentication**: 
  - Django's built-in authentication.
  - JWT (using `djangorestframework-simplejwt`) for token-based authentication.
- **Security Best Practices**:
  - SQL injection prevention.
  - Password encryption.
  - Rate-limiting API requests.
  - Educate on XSS, CSRF, and other vulnerabilities.

---

## ✅ Testing
- **Unit Testing**: Use Django's test framework to cover API endpoints, database models, and views.
- **Integration Testing**: Ensure system-wide behavior works as expected.
  
---

## 📂 Version Control & CI/CD
- **Version Control**: Git (hosted on GitHub).
- **CI/CD Pipeline**: 
  - Set up using GitHub Actions.
  - Run tests, lint checks, and auto-deploy to cloud platforms (e.g., AWS, Heroku).

---

## 🐳 Containerization
- **Dockerized Application**:
  - Containers for Django, PostgreSQL, and Redis (if caching reminders).
  - Dockerfile and `docker-compose.yml` for easy local setup.

---

## ☁️ Cloud Deployment
- **Cloud Providers**: AWS, GCP, or Heroku.
- **Production Database**: Managed PostgreSQL.
- **Environment Variables**: Use `.env` file for managing `SECRET_KEY`, database credentials, etc.
- **Bonus**: Set up Kubernetes for auto-scaling and deployment.

---

## 📊 Logging & Monitoring
- **Logging**: Leverage Django’s logging system.
- **Monitoring**: Integrate solutions like Prometheus or Sentry to track performance and errors.

---

## 📄 Technical Documentation
- **Setup Instructions**: Detailed steps to run the project locally or in production.
- **API Documentation**: Document endpoints with examples for consuming via curl, Postman, etc.
- **Code Documentation**: Inline comments and explanations for key logic and design decisions.
  
---

## 🚀 How to Run Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/mycircle.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mycircle
    ```
3. Set up the virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run database migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

---

## 📬 Contact
For questions or collaboration, feel free to reach out!

📧 Email: your.email@example.com

GitHub: [https://github.com/yourusername](https://github.com/yourusername)
