from django.shortcuts import render
from django.http import JsonResponse
from .models import Info
from django.forms.models import model_to_dict

# Create your views here.
def hello(request,*args,**kwargs):
    modeldata=Info.objects.all().order_by("?").first()
    data={}
    if modeldata:
        data=model_to_dict(modeldata)
        # data=model_to_dict(modeldata,fields=['Name','Age','City'])
    return JsonResponse(data)