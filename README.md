# README for MyLittleShop Django Project
MyLittleShop is a Django project that allows Vendor to keep records of the following:
- Vendor's sales records;
- Vendor's price list;
- Vendor's partners' info;
- Available products in vendor's storage;
- Products available in their partners' storages;

All is saved to the SQLite database.
## Installation
1. Create a virtual environment with `python -m venv venv`
1. Activate the virtual environment with `venv\scripts\activate`
1. Install required dependencies with `python -m pip install -r requirements.txt`
1. Create a superuser with `python manage.py createsuperuser`
1. Make migrations and migrate:
```
python manage.py makemigrations
python manage.py migrate
```
6. Set `DEBUG` to `False` before deploying to production.
1. Run server with `python manage.py runserver`
