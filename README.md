# Event Booking System

A Django-based web application for user registration, OTP verification, login, and event dashboard.

## Features

- User signup with OTP email verification
- Secure login and logout
- Dashboard and home page
- Responsive, styled HTML templates
- Static image support

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <https://github.com/shreenivasabv/my_project.git>
   cd <your-project-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Configure Email (for OTP)**
   - For development, add to `settings.py`:
     ```python
     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
     ```
   - For production, use SMTP settings.

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Visit [http://localhost:8000/](http://localhost:8000/) for the home page.

## Project Structure

```
accounts/
    migrations/
    static/
        home1.jpg
    templates/
        home.html
        login.html
        signup.html
        otp_verify.html
    forms.py
    models.py
    urls.py
    views.py
myproject/
    settings.py
    urls.py
README.md
```

## Screenshots

![Home Page](accounts/static/home1.jpg)

## License

MIT License

---

**Note:**  
- Place your images in the `accounts/static/` folder.
- Update email settings in `settings.py` for real OTP emails.