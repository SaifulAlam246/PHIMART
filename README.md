# Phimart – E-commerce Backend (Django REST Framework)

Phimart is a RESTful e-commerce backend built using **Django REST Framework (DRF)**. The project provides core e-commerce features such as product management, categories, carts, orders, and secure user authentication using **JWT**. API documentation is available via **Swagger** using `drf-yasg`.

---

## Features

* User authentication & authorization using **JWT (djoser + simplejwt)**
* Product management (CRUD)
* Category management
* Cart functionality (add, update, remove items)
* Order placement and order history
* Secure APIs with permission handling
* Interactive API documentation using **Swagger UI**

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** Djoser, Simple JWT
* **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
* **API Docs:** drf-yasg (Swagger & ReDoc)

---

## 📂 Project Structure (Simplified)

```
phimart/
│
├── api/
│   ├── products/
│   ├── categories/
│   ├── carts/
│   ├── orders/
│   └── urls.py
│
├── phimart/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/phimart.git
cd phimart
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Server will start at: `http://127.0.0.1:8000/`

---

## 🔐 Authentication (JWT)

This project uses **Djoser** with **JWT authentication**.


Include the access token in headers:

```
Authorization: Bearer <your_access_token>
```

---


## 📘 API Documentation (Swagger)

Swagger UI is available at:

```
/api/docs/
```

ReDoc documentation:

```
/api/redoc/
```

---

## 🧪 Testing

You can test APIs using:

* Swagger UI

---

## 🔒 Permissions

* Public access: Product & category listing
* Authenticated users: Cart & order operations
* Admin only: Product & category management

---

## 📌 Future Improvements

* Payment gateway integration
* Product reviews & ratings
* Wishlist feature
* Role-based access control
* Caching for performance optimization

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Saiful Alam**
Backend Developer | Django REST Framework
