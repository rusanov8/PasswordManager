# Password Manager

Simple Django application for managing passwords.

## Installation

1. Make sure you have Python 3.x installed.
2. Clone the repository:

```bash
git clone git@github.com:rusanov8/PasswordManager.git
```
3. Navigate to the project directory:
```
cd PasswordManager
```
4. Install dependencies:
```
pip install -r requirements.txt
```

5. Create a .env file and configure environment variables:
```
SECRET_KEY=your_secret_key

# DataBase
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
```

6. Apply migrations:
```
python manage.py migrate
```
7. Run the server:
```
python manage.py runserver
```
8. Open http://localhost:8000 in your browser.


## Docker

1. Create your `.env.docker` file based on `.env.docker.example` and configure environment variables for the database:

2. Run the application using Docker Compose:
```
docker-compose up --build
```

3. Open http://localhost:8000 in your browser.



### Usage
After installing the application, you can create or update passwords for various services. Use the web interface or API to interact with the application.

