### 1] INSTALLED_APPS = [
    'rest_framework',
]

### 2] To Import Filters Globaly In Settings.py File
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 100
}
```
### 3]Simpaly Hit That URL  http://localhost:8000/api/

# CursorPagination style only presents Privios and Next controls 

# In We Cursor Paginnation We Have Specify The Ordering Filed,Because In Cursor Pagination Order Data Default using creted fielss i case if in our data creted field are not present Then we Have To Specify The Ordering fields
    ordering='Name'






# If We Have To Change The The Cursor String -->(http://127.0.0.1:8000/api/?cursor=cD1HYXVyYW5n)
    cursor_query_param='page'              # -->(http://127.0.0.1:8000/api/?page=cD1HYXVyYW5n)

