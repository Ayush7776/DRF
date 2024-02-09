from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import InfoSerializer
from .models import Info


class InfoApiView(APIView):

    def get(self,request):
        getdata=Info.objects.all()
        serializer=InfoSerializer(getdata,many=True)
        return Response({'Massage':serializer.data})
        return Response({'Massage':serializer.errors})

    def post(self,request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Massage':serializer.data})
        return Response({'Massage':serializer.errors})

    def put(self,request):
        getdata=Info.objects.get(id=request.data['id'])
        serializer=InfoSerializer(getdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Massage':serializer.data})
        return Response({'error':serializer.errors})

    def patch(self,request):
        getdata=Info.objects.get(id=request.data['id'])
        serializer=InfoSerializer(getdata,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Massage':serializer.data})
        return Response({'error':serializer.errors})
   
    def delete(self,request):
        getdata=Info.objects.get(id=request.data['id'])
        if getdata:
            getdata.delete()
            return Response({'Massage':"Data Deleted SuccessFully.."})
        return Response({'Massage':"User Not Found.."})


































































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









    