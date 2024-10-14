from django.shortcuts import render
from imagegallery.models import imggal

def imagedisplay(request):
    resultdisplay = imggal.objects.all()
    return render(request, 'index.html', {'imggal':resultdisplay})