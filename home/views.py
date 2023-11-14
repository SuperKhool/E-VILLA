from django.shortcuts import render ,redirect
from product.models import *
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    all_cata=catagory.objects.all()
    productss=products.objects.all()
    return render(request,'home/index.html',locals())
def contact(request):
    if request.method=="POST":
        nam=request.POST.get('nam')
        phone=request.POST.get('phone')
        mail=request.POST.get('mail')
        msg=request.POST.get('msg')
        print(nam)
        print(phone)
        all_con=feedback.objects.create(name=nam,phone=phone,mail=mail,msg=msg)
        all_con.save()
        messages.success(request,"Your FeedBack Is Send To the Admin")
        return redirect('index')
    
        
             
    return render(request,'home/contact.html',locals())
def blog(request):
    return render(request,'home/blog.html')
def about(request):
    return render(request,'home/about.html')
def b1(request):
    return render(request,'home/b1.html')
def b2(request):
    return render(request,'home/b2.html')
def b3(request):
    return render(request,'home/b3.html')