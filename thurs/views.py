from django.shortcuts import render
from django.http import HttpResponse
from thurs.forms import *
from thurs.models import *

# Create your views here.


def insert_topic(request):
    TMFO=Topicmodelforms()
    d={'TMFO':TMFO}

    if request.method =='POST':
        TMFOD=Topicmodelforms(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WPMFO=Webpagemodelforms()
    d={'WPMFO':WPMFO}

    if request.method=='POST':
        WPMFOD=Webpagemodelforms(request.POST)
        if WPMFOD.is_valid():
            WPMFOD.save()
            return HttpResponse('inserted webpage')

    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    ARMFO=Accessrecordsmodelforms()
    d={'ARMFO':ARMFO}

    if request.method=='POST':
        ARMFOD=Accessrecordsmodelforms(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse('accessrecords inserted')
    return render(request,'insert_accessrecords.html',d)