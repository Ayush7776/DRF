from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import Info
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
class InfoApiView(ListAPIView):
    queryset=Info.objects.all()
    serializer_class=InfoSerializer
    filter_backends=[DjangoFilterBackend]

    # filterset_fields=['Admin']
    # http://127.0.0.1:8000/api/?Admin=Neha
    
    filterset_fields=['Admin','Name']
    # http://127.0.0.1:8000/api/?Admin=Neha&Name=Gaurang

    

































































# @api_view(['GET'])
# def hello(request):
#     modeldata=Info.objects.all()
#     serializerdata=InfoSerializer(modeldata,many=True)
#     return Response({'data':serializerdata.data})

# @api_view(['POST'])
# def hi(request):
#     serializer=InfoSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'massage':serializer.errors})
#     serializer.save()
#     return Response({'massage':serializer.data})

# # Compleate Update
# @api_view(['PUT'])
# def update(request,id):
#     try:
#         getdata=Info.objects.get(id=id)
#         serializer=InfoSerializer(getdata,data=request.data)
#         if not serializer.is_valid():
#             return Response({'error':serializer.errors})
#         serializer.save()
#         return Response({'massage':serializer.data})
#     except Exception as e:
#         print(e)
#         return Response({'massage':'Some Error Occurd..'})

# @api_view(['PATCH'])
# def miniupdate(request,id):
#         getdata=Info.objects.get(id=id)
#         serializer=InfoSerializer(getdata,data=request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'error':serializer.errors})
#         serializer.save()
#         return Response({'massage':serializer.data})

# @api_view(['DELETE'])
# def remove(request,id):
#     try:
#         getdata=Info.objects.get(id=id)
#         if getdata:
#             getdata.delete()
#             return Response({'massage':'User Sucessfully Removed'})
#     except:
#         return Response({'massage':'No User Found'})









    