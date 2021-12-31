from django.shortcuts import render
from .forms import imgform
from .models import img
# Create your views here.
def home(request):
    if request.method=='POST':
        dic=imgform(request.POST,request.FILES)
        if dic.is_valid():
            dic.save()
    dic=imgform()
    images=img.objects.all()
    return render(request,'core/home.html',{'form':dic,'img':images})