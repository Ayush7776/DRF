from rest_framework.pagination import LimitOffsetPagination

class MyPagination(LimitOffsetPagination):
    
    # How Many Records Will Display In In Singal Page That Will Deside Limit Attribute
    default_limit=3

    # If We Have To Change The The page Name -->(http://localhost:8000/api/?limit=2)
    limit_query_param='page'             #  -->(http://localhost:8000/api/?page=2)

    # Fectch Records Acording To Your Need Where We Want To Start From Perticular Record 
    # http://localhost:8000/api/?page=1&offset=4
    
    
    # offset_query_param Use To Change The if we Have To Change offset String
    offset_query_param='records'
    # Before http://localhost:8000/api/?page=1&offset=4
    # After  http://localhost:8000/api/?page=1&records=4

    # We Can Set maximum How Many Records Maximum Fetch User
    max_page_size = 4
    # http://localhost:8000/api/?page=1&records=4 It Work 
    # http://localhost:8000/api/?page=1&records=5 It Will Not Work
    