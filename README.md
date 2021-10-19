# django-audit


![GitHub issues](https://img.shields.io/github/issues/Emmarex/django-audit)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dj_audit)
![Codecov](https://img.shields.io/codecov/c/github/Emmarex/django-audit)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

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

## Management commands

```flush_auditlog``` - Cleans up dj-audit AuditLog table

```bash
python manage.py flush_auditlog
```

## Test

```bash
make test
```

or with coverage

```bash
make coverage_test
```
