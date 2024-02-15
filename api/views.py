from rest_framework.response import Response
from rest_framework import generics
from .serializer import *
from .models import Info

# generics.ListAPIView For Get Method
# genirics.CreateAPIView For Post Method
# genirics.ListCreateAPIView For Both Abou Method

class InfoGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class=InfoSerializer
# generics.RetrieveAPIView For Get Specific Data By ID
# generics.UpdateAPIView For Put Method
# genirics.DestroyAPIView For Delete Method
class InfoGeneric2(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class=InfoSerializer
    lookup_field='id'
    






























































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









    