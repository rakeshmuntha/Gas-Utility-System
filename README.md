# Gas Utility System

This Django-based web application is designed to manage consumer services for a gas utility company. The system allows customers to submit, track, and manage their service requests efficiently. Additionally, customer support representatives can manage requests to ensure seamless customer service.

## Features

### For Customers

Service Request Submission:

* Select the type of service request.

* Provide detailed information about the request.

* Upload attachments if needed.

### Request Tracking:

* View the status of submitted requests.

* Check submission and resolution timestamps.

### User Authentication:

* Secure registration and login system.

* For Admin (Support Representatives)

### Admin Panel Management:

* View all customer requests.

* Update request status for better customer communication.

### Output ScreenShots:
<img width="400" alt="Screenshot 2025-03-27 at 4 48 37 PM" src="https://github.com/user-attachments/assets/406a4eaa-40a0-47c4-8fc3-c88d8b68260f" />
<img width="400" alt="Screenshot 2025-03-27 at 3 51 01 PM" src="https://github.com/user-attachments/assets/c634f32a-d480-43f7-a49a-a90485e1ddb2" />
<img width="400" alt="Screenshot 2025-03-27 at 3 50 51 PM" src="https://github.com/user-attachments/assets/b9640ec5-24aa-4e27-8d08-62a6afb8d9a9" />
<img width="400" alt="Screenshot 2025-03-27 at 3 51 59 PM" src="https://github.com/user-attachments/assets/d824136a-14d3-4d5b-834f-a69389785800" />
<img width="400" alt="Screenshot 2025-03-27 at 3 52 12 PM" src="https://github.com/user-attachments/assets/19a095b9-7490-490d-adf8-87b57bc95d29" />
<img width="400" alt="Screenshot 2025-03-27 at 3 52 26 PM" src="https://github.com/user-attachments/assets/c28e0f0f-2397-43d6-83cd-a9ea784dd849" />
<img width="400" alt="Screenshot 2025-03-27 at 3 52 35 PM" src="https://github.com/user-attachments/assets/005fa7fe-86b8-48cb-b75c-cc58feb1d0da" />
<img width="400" alt="Screenshot 2025-03-27 at 3 53 02 PM" src="https://github.com/user-attachments/assets/ff3c91df-f6da-462e-b3da-d15f9299a1cb" />


## Tech Stacks:

Python (Django Framework)

HTML5, CSS3, JavaScript (for UI)

SQLite (Database)

Installation Guide

## Clone the Repository

```
 git clone https://github.com/rakeshmuntha/gas-utility-system.git
```   

```cd gas-utility-system```

## Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # (For Linux/Mac)
venv\Scripts\activate     # (For Windows)

### Install Dependencies

pip install -r requirements.txt

### Directory Structure
```
├── gasutility
│   ├── services
│   │   ├── migrations
│   │   ├── static
│   │   │   └── css
│   │   │       └── style.css
│   │   ├── templates
│   │   │   └── services
│   │   │       ├── home.html
│   │   │       ├── submit_request.html
│   │   │       ├── track_requests.html
│   │   ├── urls.py
│   │   ├── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt

```


### Database Migration

```
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser for Admin Access

```python manage.py createsuperuser```

### Run the Development Server

```python manage.py runserver```

## Usage Guide

### Customer Actions:

* Register/Login as a customer.

* Submit a service request using the "Submit Request" page.

* Track request status through the "Track Requests" page.

### Admin Actions:

* Login to the admin panel.

* View all customer requests.

* Update request status to keep customers informed.

