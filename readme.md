### 1] INSTALLED_APPS = [
    'rest_framework',
]

### 2] To Import Filters Globaly In Settings.py File
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```
### 3]Simpaly Hit That URL  http://localhost:8000/api/?page=2

