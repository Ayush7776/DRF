from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    
    # How Many Records Will Display In In Singal Page 
    page_size=3

    # If We Have To Change The The page Name -->(http://localhost:8000/api/?page=2)
    page_query_param='Pageno'             #  -->(http://localhost:8000/api/?Pageno=2)

    # If We Have To Take Permission To User Fectch Records Acording To Your Need
    # http://localhost:8000/api/?Pageno=1&records=4
    page_size_query_param='records'

    # We Can Set maximum How Many Records Maximum Fetch User
    max_page_size = 4
    # http://localhost:8000/api/?Pageno=1&records=4 It Work 
    # http://localhost:8000/api/?Pageno=1&records=5 It Will Not Work
    