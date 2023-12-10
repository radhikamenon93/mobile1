from django.shortcuts import render,redirect
from django.views.generic import View
from works.forms import Mform
from works.models import Mobile
from django.contrib import messages

# Create your views here.
class Mobileview(View):
    def get(self,request):
        form=Mform()
        return render(request,"mob.html",{"form":form})
    def post(self,request):
        form=Mform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"brand added successfully")
            form=Mform()
            return render(request,"mob.html",{"form":form})
           
            
        else:
            messages.error(request,"retry")
            return render(request,"mob.html",{"form":form})  

class Moblist(View):
    def get(self,request):
        qs=Mobile.objects.all()
        return render(request,"moblist.html",{"qs":qs})

    def post(self,request):
        b=request.POST.get("p")
        qs=Mobile.objects.filter(brand=b)
        return render(request,"moblist.html",{"qs":qs})


class Mobdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk") 
        Mobile.objects.get(id=id).delete()
        return redirect('book-al')  

class Mobupdate(View):
    def get(self,request,*args,**kwargs):
        k=kwargs.get("pk") 
        obj=Mobile.objects.get(id=k)
        form=Mform(instance=obj)
        return render(request,"mobedit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        k=kwargs.get("pk")    
        obj=Mobile.objects.get(id=k)
        form=Mform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        else:
            print("bye")
        return redirect("book-al")        



         


            

