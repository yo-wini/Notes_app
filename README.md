# 📝 FastAPI Notes App with JWT Authentication

A simple RESTful API built with **FastAPI**, **SQLModel**, and **JWT Authentication** that allows users to register, login, and perform CRUD operations on personal notes.

---

## 🚀 Features
- ✅ **User Registration**
- ✅ **User Login with JWT Token**
- ✅ **Protected Routes for Notes CRUD (Create, Read, Update, Delete)**
- ✅ **SQLite Database with SQLModel ORM**
- ✅ **Swagger/OpenAPI Documentation**
- ✅ **JWT-based Authorization with Bearer Token**

---

## 📂 Project Structure
/auth
├── routes.py # User Auth Routes (Register/Login)
├── notes_routes.py # Notes CRUD Routes with Auth
├── models.py # User & Note Models
├── utils.py # Auth Utils (Hashing/JWT)
database.py # Database Connection & Session
main.py # FastAPI App & Router Inclusion


---

## 🛠️ Technologies Used
- **FastAPI** - Web framework
- **SQLModel** - ORM for database models
- **SQLite** - Lightweight Database
- **PyJWT / jose** - JWT Token Handling
- **Passlib** - Password Hashing
- **Swagger Docs** - Auto API Docs

---

## 📥 Setup & Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-notes-app.git
cd fastapi-notes-app


📝 Notes CRUD Endpoints (Authenticated)
Method	Endpoint	Description
POST	/notes/	Create a new note
PUT	/notes/{note_id}	Update an existing note
DELETE	/notes/{note_id}	Delete a note

🧩 Future Improvements (Optional)
 Use Alembic for DB migrations

 Token Refresh with OAuth2

 Add Pagination to Notes

 Deploy with Docker

