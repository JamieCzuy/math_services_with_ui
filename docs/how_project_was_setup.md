# how_project_was_setup

## Steps to setup the project

1. Create and activate virtual environment:

    ```bash
    python -m venv venv
    source ./venv/bin/activate
    ```

2. Check that nothing is installed yet:

    ```bash
    pip list
    ```

3. Upgrade pip to remove annoying update reminder:

    ```bash
    pip install --upgrade pip
    ```

4. Create requirements.txt:

    ```txt
    Django==4.2
    pytest==8.3.3
    ```

5. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Use `django-admin startproject` to create the Django project:

    ```bash
    django-admin startproject math_services .
    ```

7. Use `django-admin startapp` to create the Services app:

    ```bash
    django-admin startapp services
    ```

8. Add new services app to installed apps:

    In `./math_services/settings.py` add 'services' after line 39 to make `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'services',
    ]
    ```

9. Run `./manage.py migrate` to initialize the Sqlite3 database.

10. Run django and open in a browser to check that it is running:

    ```bash
    ./manage.py runserver 0.0.0.0:8000
    ```

    ```bash
    # In a browser open
    http://localhost:8000
    ```

11. Now the coding can begin!
