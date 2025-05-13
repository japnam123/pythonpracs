# Django Project Template

A modern Django project template with common configurations and best practices.

## Features

- Django 5.0.2
- User authentication with django-allauth
- Bootstrap 5 styling with crispy-forms
- PostgreSQL database support
- Debug toolbar for development
- Static file handling with whitenoise
- Production-ready with gunicorn
- Environment variable management with python-dotenv

## Prerequisites

- Python 3.8 or higher
- PostgreSQL (for production)
- Git

## Installation Guide

1. **Clone the repository**
```bash
git clone <repository-url>
cd django_project
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```bash
# Django settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Email settings (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see your application.

## Project Structure

```
django_project/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── core/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   ├── home/
│   └── common/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── home/
│   └── accounts/
└── media/
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project uses flake8 for code linting:
```bash
flake8 .
```

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations status
python manage.py showmigrations
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic
```

## Deployment

1. **Update settings**
- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS`
- Update database settings
- Set up static and media file serving

2. **Collect static files**
```bash
python manage.py collectstatic
```

3. **Run with gunicorn**
```bash
gunicorn core.wsgi:application
```

## Security Considerations

1. **Environment Variables**
- Never commit `.env` file
- Use strong secret keys
- Keep database credentials secure

2. **Django Security**
- Keep Django and dependencies updated
- Use HTTPS in production
- Implement proper authentication
- Configure CORS settings

3. **Database Security**
- Use strong passwords
- Limit database user permissions
- Regular backups

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 