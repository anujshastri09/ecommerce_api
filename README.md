#  E-Commerce Backend API

##  Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite

##  Features
- User Registration & Login (JWT)
- Role-based Access Control (Admin/Customer)
- Product Management (CRUD APIs)
- Cart System (Add, Update, Remove)
- Order System with Transaction Safety
- Order History

## Authentication
JWT-based authentication using access & refresh tokens.

##  API Endpoints

### Auth
- POST /api/accounts/register/
- POST /api/token/

### Products
- GET /api/products/
- POST /api/products/ (Admin)

### Cart
- POST /api/cart/add/
- GET /api/cart/
- PUT /api/cart/update/<id>/
- DELETE /api/cart/remove/<id>/

### Orders
- POST /api/orders/place/
- GET /api/orders/

## Key Highlights
- Transaction-safe order processing
- Optimized queries & pagination
- Clean modular architecture