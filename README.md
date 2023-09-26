# MY DJANGO WEBSITE

## Getting started

Clone this repository and enter the project containing folder

```bash
git clone <repo-url>
cd repo-dir
```

Create your pyenv

```bash
python3 -m venv venv 
```

Activate your pyenv

```bash
source venv/bin/activate
```

Install all required dependencies

```bash
pip3 install -r requirements.txt
```

Run migrations

```bash
python3 manage.py migrate
```

## Running

Run the Django web server locally

```bash
python3 manage.py runserver
```

Check out your first website on [http://localhost:8000](http://localhost:8000)

## Admin

Create superuser to manage your database information

```bash
python manage.py createsuperuser
```

Check out your admin page on [http://localhost:8000/admin](http://localhost:8000/admin)
