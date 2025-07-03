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
