## Filter Using Generic ListAPIView
```bash
pip install django_filter
```
### 2] INSTALLED_APPS = [
    'django_filters',
]

### 3] To Import Filters Globaly In Settings.py File
```
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```