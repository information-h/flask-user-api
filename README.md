markdown
# 🧩 Simple Flask User Management API

This is a basic Flask RESTful API for managing users using an in-memory list (like a temporary database). It supports operations to **get**, **create**, **retrieve by ID**, and **delete** users.

---

## 🚀 Features

- `GET /user` – Get all users  
- `GET /user/<id>` – Get a user by ID  
- `POST /user` – Create a new user  
- `DELETE /user/<id>` – Delete a user by ID  

---

## 📂 Technologies Used

- Python 3.x
- Flask

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install flask
````

### 2. Run the app

```bash
python api.py
```

The API will be available at:
📍 `http://127.0.0.1:5000/`

---

## 🧪 API Usage

### 🔹 GET all users

```http
GET /user
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "akash",
    "email": "akashkumarshuk805133@gmail.com"
  },
  {
    "id": 2,
    "name": "jagesh",
    "email": "jageshshukla222@gmail.com"
  }
]
```

---

### 🔹 POST a new user

```http
POST /user
Content-Type: application/json
```

**Body:**

```json
{
  "name": "rahul",
  "email": "rahul123@gmail.com"
}
```

**Response:**

```json
{
  "id": 3,
  "name": "rahul",
  "email": "rahul123@gmail.com"
}
```

---

### 🔹 GET a user by ID

```http
GET /user/1
```

**Response:**

```json
{
  "id": 1,
  "name": "akash",
  "email": "akashkumarshuk805133@gmail.com"
}
```

---

### 🔹 DELETE a user by ID

```http
DELETE /user/2
```

**Response:**

```http
204 No Content
```

---

## 🖼️ Screenshots

> 🔻 Replace the image links below with your screenshots taken from Postman, browser, or terminal.

### ✅ GET all users

![GET /user](screenshots/get_users.png)

### ✅ POST new user

![POST /user](screenshots/post_user.png)

### ✅ DELETE user

![DELETE /user](screenshots/delete_user.png)

---

## 📄 License

This project is open source and free to use.

---

```

---

### ✅ Next Steps:
1. Save this content into a file named `README.md`.
2. Create a `screenshots/` folder in your repo and add screenshots with filenames like `get_users.png`, etc.
3. Push it to GitHub.

Would you like me to generate fake screenshot images for demo purposes?
```
