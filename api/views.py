from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .models import *

@api_view(['GET'])
def hello(request):
    modeldata=Info.objects.all()
    serializerdata=InfoSerializer(modeldata,many=True)
    return Response({'data':serializerdata.data})

@api_view(['POST'])
def hi(request):
    serializer=InfoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'massage':serializer.errors})
    serializer.save()
    return Response({'massage':serializer.data})
    


















    