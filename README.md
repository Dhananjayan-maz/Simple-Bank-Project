# 🏦 Bank Management System

A secure and web-based banking application developed using Django that enables users to perform essential banking operations such as account management, deposits, withdrawals, and transaction tracking through an interactive dashboard.

---

## 📌 Project Overview

The Bank Management System is designed to simulate core banking functionalities in a secure and structured environment. The system provides user authentication, account handling, transaction processing, and administrative management features.

The application supports role-based access where users can manage personal banking operations while administrators can monitor users, accounts, and transactions through the Django admin panel.

---

## ✨ Key Features

### 🔹 User Authentication
- User Signup and Login system
- Secure password hashing using Django Authentication
- Session management and logout functionality
- Protected user dashboards

### 🔹 Banking Operations
- Deposit money into accounts
- Withdraw account balance
- Check available account balance
- Maintain transaction history
- Account information dashboard

### 🔹 Transaction Management
- Store transaction records securely
- Track deposits and withdrawals
- User-wise transaction monitoring
- Database-driven account updates

### 🔹 Admin Panel
- Manage registered users
- Monitor banking accounts
- View all transaction records
- Django admin-based management interface

### 🔹 UI & User Experience
- Responsive dashboard interface
- Clean navigation and forms
- Interactive banking workflow
- User-friendly design

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend
- Django
- Python

### Database
- SQLite / MySQL

### Development Tools
- VS Code
- GitHub

---

## ⚙️ System Workflow

```text
User Registration / Login
            ↓
      Access Dashboard
            ↓
 Perform Banking Operations
            ↓
 Deposit / Withdraw Amount
            ↓
 Update Account Balance
            ↓
 Store Transaction Records
            ↓
 Display Transaction History
```

---

## 🧠 Project Architecture

```text
                ┌─────────────────┐
                │ User Interface  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Django Backend  │
                └────────┬────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│ Authentication  │           │ Banking Logic   │
│ System          │           │ Transactions    │
└────────┬────────┘           └────────┬────────┘
         │                               │
         ▼                               ▼
┌─────────────────────────────────────────────┐
│              Database Storage               │
└─────────────────────────────────────────────┘
```

---

## 📸 Project Screenshots

### 🏠 Home Page
<img width="1366" height="685" alt="index" src="https://github.com/user-attachments/assets/77e58a74-88c7-43db-8945-467f6c451134" />

### 📊 User Dashboard
<img width="1366" height="686" alt="dashboard" src="https://github.com/user-attachments/assets/97a93b21-2023-4d51-b716-933167b6bee0" />

### 💰 Deposit Operation
<img width="1366" height="690" alt="deposite" src="https://github.com/user-attachments/assets/f144e8d8-e950-414f-9809-ac3168c32661" />

---

## 📂 Project Structure

```text
bank/

├── manage.py
├── bank/                     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/                    # Main application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │   ├── deposit.html
│   │   ├── withdraw.html
│   │   └── transactions.html
│   │
│   └── static/
│
├── media/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## 🔒 Security Features

- Secure password hashing
- Session-based authentication
- CSRF protection enabled
- Django ORM for secure database operations

---

## 🎯 Core Functionalities

- User Registration & Login
- Deposit and Withdrawal Operations
- Account Balance Management
- Transaction History Tracking
- Admin-based User Management

---

## 🔮 Future Enhancements

- Online money transfer
- OTP verification system
- Email notifications
- PDF transaction statements
- Banking analytics dashboard
- Payment gateway integration
