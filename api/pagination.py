from rest_framework.pagination import CursorPagination

class MyPagination(CursorPagination):
    
    # How Many Records Will Display In In Singal Page That Will Deside Limit Attribute
    page_size=3
    # In We Cursor Paginnation We Have Specify The Ordering Filed,Because In Cursor Pagination Order Data Default using creted fielss i case if in our data creted field are not present Then we Have To Specify The Ordering fields
    ordering='Name'
    

    # If We Have To Change The The Cursor String -->(http://127.0.0.1:8000/api/?cursor=cD1HYXVyYW5n)
    cursor_query_param='page'                 #  -->(http://127.0.0.1:8000/api/?page=cD1HYXVyYW5n)

   