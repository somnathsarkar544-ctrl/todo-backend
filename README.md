# 📝 Todo API (Django REST Framework + JWT)

A secure and user–specific Todo API built using Django REST Framework (DRF).  
Each user can only access their own todos using JWT authentication.

---

## 🚀 Features
- JWT Authentication (login to get access token)
- Create Todos
- Update Todos
- Delete Todos
- Get todos of logged-in user only
- Secure API (IsAuthenticated)
- Clean & production-ready code structure

---

## 📌 Base URL
```
http://127.0.0.1:8000/api/
```

---

## 🔐 Authentication

### *Login to get JWT tokens*
```
POST/api/token/
```
*Body:*
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
You will receive
```
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Use Access Token in Header
```
Authorization: Bearer <access_token>
```

## 📝Todo Endpoints
## ✔️Get all Todos(user-specific)
```
   GET/api/todos/
```
   
## ✔️Create a Todo
```
   POST /api/todos/
```
 *Body:*
   ```json
   {
  "title": "My Task",
  "completed": false
 }
 ```
## ✔️Update todo
```
   PUT /api/todos/<id>/
```

## ❌Delete Todo
```
   DELETE /api/todos/<id>/
```

## 🧱Todo Model
 ```python
   class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
```
    
## ⚙️Setup Instructions 
```
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
```
  
## 📂Project Structure
```
   myapi/
   todo/
   manage.py
```


## 🤝For Frontend Developers
⚫ All endpoints a valid JWT access token.
⚫ Use /api/token/ to login and get a token
⚫ All todos belong to the authenticated user.


---

## 🚀 Ready for Integration

This backend is fully ready to be used by any frontend such as *React, **Next.js, **Flutter, **Android, or **Vue*.

Just use the JWT *access token* to authenticate and call the Todo API endpoints.

Feel free to use this project for:
- Your portfolio  
- Learning backend development  
- Building a full-stack app  
- Team projects

## 🛠 Tech Stack

- *Python 3*
- *Django*
- *Django REST Framework*
- *JWT Authentication (SimpleJWT)*
- *SQLite (default)*







