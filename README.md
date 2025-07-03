# 🎟️ Event Registration System (Django REST Framework)

A full-featured backend API for managing events and user registrations built using Django REST Framework and JWT authentication.

---

## 🚀 Features

- User registration via JWT authentication
- Create, update, delete events (by organizers only)
- Public event listing and detail view
- Event registration for authenticated users
- Users can view or cancel their registrations
- Admin panel for event and registration management

---

## 🧱 Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Database**: PostgreSQL (or SQLite for development)
- **Tools**: Postman, pgAdmin, Python 3.13+

---

## 📂 Project Structure

event_project/
- ├── event_project/ # Django project settings
- ├── event/ # Django app: event + registration logic
- ├── env/ # Virtual environment (not tracked)
- ├── manage.py
- └── README.md
Authentication (JWT)
- Get Access Token
- POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
- Use the token in headers
- Authorization: Bearer your_access_token
- 
**API Endpoints**
-   Endpoint	Method	Auth?	Description
- /api/events/	GET	❌	List all events
- /api/events/	POST	✅	Create new event
- /api/events/<id>/	GET	❌	Get event details
- /api/events/<id>/	PUT/DELETE	✅	Edit/delete (only organizer)
- /api/events/<id>/register/	POST	✅	Register for event
- /api/registrations/	GET	✅	List user’s registrations
- /api/registrations/	DELETE	✅	Cancel registration
- /api/token/	POST	❌	Get JWT token
- /api/token/refresh/	POST	❌	Refresh access token


# 🔗 Simple URL Shortener Backend (Flask)

A minimal Flask-based backend server for shortening long URLs. It generates unique short codes for original URLs and supports redirection.

---

## 🚀 Features

- API to shorten long URLs
- Auto-generates unique short codes
- Stores mappings in SQLite
- Redirects short URL to original link
- (Optional) Basic frontend UI for shortening

---

## 🧱 Tech Stack

- **Backend**: Flask
- **Database**: SQLite (default) or MongoDB (optional)
- **Language**: Python 3.13+
- **Frontend (optional)**: HTML + JS

---

## 📂 Project Structure

URL_SHORTNER_PROJECT/
├── app.py # Flask app
├── urls.db # SQLite database (auto-created)
├── templates/ # Optional: HTML UI
│ └── base.html
│ └── index.html
│ └── shorturl.html
└── README.md

**API Endpoints**
**🔸 1. Shorten a URL**
POST /shorten

Request body (JSON):

{
  "long_url": "https://www.example.com/very/long/url"
}
Response:
{
  "short_url": "http://localhost:5000/abc123"
}

**🔸 2. Redirect to long URL**
GET /<short_code>

Accessing:
http://localhost:5000/abc123

Redirects to:
https://www.example.com/very/long/url

**How It Works**
- Generates a random 6-character code for each new URL.
- Stores the mapping of code → long URL in SQLite.
- If a code already exists, it reuses it.
- Uses Flask's redirect functionality to handle redirection.
  
**Frontend UI**
- Add an index.html in templates/ for a simple form.
- Users can enter long URLs and get a short one on the page.
- Use fetch() or axios to call the /shorten API.
  
