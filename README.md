# Social Networking Application API

This is a Django REST Framework based API for a social networking application.

## Installation

### Prerequisites

- Python (3.8+)
- pip
- Docker (if running with Docker)

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd social_network
2. Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3.Install dependencies:

bash
Copy code
pip install -r requirements.txt

4.Apply database migrations:

bash
Copy code
python manage.py migrate
5. Create a superuser:

bash
Copy code
python manage.py createsuperuser
6.Run the development server:

bash
Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/

7. API Endpoints
Signup: /signup/ (POST)
Login: /login/ (POST)
Refresh Token: /token/refresh/ (POST)
User Search: /api/search/?q=query (GET)
Friend Requests: /api/friend-requests/ (GET, POST, PUT, PATCH, DELETE)
Accept Friend Request: /api/friend-requests/{id}/accept/ (POST)
Reject Friend Request: /api/friend-requests/{id}/reject/ (POST)
List Friends: /api/friends/ (GET)
List Pending Requests: /api/pending-requests/ (GET)
