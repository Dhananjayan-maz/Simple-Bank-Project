🏦 Bank Management Website

A simple and secure Bank Web Application built using Django, providing essential banking operations such as user authentication, account management, and basic money transactions.

✨ Features

// User Authentication

-User Signup (create account)

-User Signin (login)

-Secure password hashing using Django's auth system

-Logout functionality


// Banking Operations

-Deposit Money

-Withdraw Money

-Check Account Balance

-View Transaction History

-Simple dashboard to view account info


// Admin Panel

-Manage users

-Manage accounts

-View all transactions

-Django default admin interface


📁 Project Structure (Simplified)

bank/

│── bank/                
│── myapp/            
│── media/        
│── templates/           
│── static/            
│── manage.py/

│── venv

//Installation & Setup

1. Create Virtual Environment

  python -m venv venv

2. Activate Virtual Environment

  Windows

  venv\Scripts\activate

3. Install Requirements
   
  pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run the Server
   
python manage.py runserver

Now open your browser at:

👉 http://127.0.0.1:8000/

6.Default Credentials (for Demo)

  You can create a Django superuser:

  python manage.py createsuperuser

//Technologies Used

-Python 3

-Django

-HTML, CSS, Bootstrap

-SQLite / MySQL

-Django ORM


📜 License

  This project is for educational and personal use.

<img width="1366" height="685" alt="index" src="https://github.com/user-attachments/assets/77e58a74-88c7-43db-8945-467f6c451134" />
<img width="1366" height="686" alt="dashboard" src="https://github.com/user-attachments/assets/97a93b21-2023-4d51-b716-933167b6bee0" />
<img width="1366" height="690" alt="deposite" src="https://github.com/user-attachments/assets/f144e8d8-e950-414f-9809-ac3168c32661" />
