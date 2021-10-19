# django-audit


![GitHub issues](https://img.shields.io/github/issues/Emmarex/django-audit)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dj_audit)
![Codecov](https://img.shields.io/codecov/c/github/Emmarex/django-audit)

Django Audit is a simple Django app that tracks and logs requests to your application.

## Quick Start

1. Install django-audit

```bash 
pip install dj-audit
```

2. Add ```dj_audit``` to your INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...,
    "dj_audit"
]
```

3. Add ```dj_audit``` middleware:

```python
MIDDLEWARE = [
    ...
    "dj_audit.middleware.AuditMiddleware"
]
```

4. Run migrate

```bash
python manage.py migrate
```

## Test

```bash
PYTHONPATH=$PYTHONPATH:$PWD django-admin test dj_audit --settings=dj_audit.test_settings
```