# FastAPI Learning

Learning FastAPI and Pydantic through practical projects, REST API development, data validation, request handling, and backend best practices.

---

## About

This repository documents my journey of learning **FastAPI** and **Pydantic** by building hands-on projects and exploring modern backend development concepts.

Topics covered include:

- FastAPI Fundamentals
- API Routing
- Query Parameters
- Path Parameters
- Request & Response Models
- Data Validation with Pydantic
- JSON Handling
- Error Handling
- HTTP Status Codes
- CRUD Operations
- REST API Design
- Backend Best Practices

---

## Repository Structure

```text
fastapi-learning/
│
├── docs/
│   └── fast-api-notes.pdf
│
├── patient-records-api/
│   │
│   ├── main.py
│   ├── patients.json
│   ├── README.md
│   └── .gitignore
│
└── README.md
```

---

## Projects

### 1. Patient Records API

A simple REST API built using FastAPI to practice:

- GET Endpoints
- Path Parameters
- Query Parameters
- Data Filtering
- Sorting
- JSON Data Handling
- Error Handling
- BMI Calculation

Project Location:

```text
patient-records-api/
```

---

## Documentation

Learning notes and reference material:

```text
docs/fast-api-notes.pdf
```

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-username>/fastapi-learning.git
cd fastapi-learning
```

### Create a Virtual Environment

```bash
python -m venv myenv
```

### Activate the Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux/macOS:

```bash
source myenv/bin/activate
```


### Run the Application

```bash
cd patient-records-api
uvicorn main:app --reload
```

---

## API Documentation

Once the server is running, visit:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```


## Learning Goals

- Build REST APIs with FastAPI
- Understand Pydantic models and validation
- Learn API design principles
- Explore backend development workflows
- Develop production-ready Python API skills

---

## Future Additions

- Authentication & Authorization
- JWT Tokens
- Database Integration
- SQLAlchemy
- PostgreSQL
- File Upload APIs
- Dependency Injection
- Testing with Pytest
- Docker Deployment
- CI/CD Pipelines

---

## 👨‍💻 Author  
**Mohd Uzaif**  
🎓 *M.Tech (AI & ML), Jamia Millia Islamia University*   
---

Learning and building modern backend applications with FastAPI.