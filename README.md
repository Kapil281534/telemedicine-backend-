# Telemedicine Backend Assignment

## Features
- User Registration and Login with JWT
- Doctor and Patient roles with CRUD
- Appointment creation and listing
- WebSocket for real-time doctor status
- Swagger UI documentation

## Technologies
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- WebSocket
- Swagger UI

## Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/telemedicine-backend.git
cd telemedicine-backend
python -m venv venv
venv\Scripts\activate       # For Windows
pip install -r requirements.txt
uvicorn main:app --reload
