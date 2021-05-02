from django.shortcuts import render
from .models import Checkin

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class EmpView(TemplateView):
    def post(self, request, *args, **kwargs):
        button = request.POST["b1"]
        if button == "Insert":
            id = request.POST["t1"]
            
            name = request.POST["t2"]
            addr = request.POST["t3"]
            age = request.POST["t4"]
            gender = request.POST["gender"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            adult = request.POST["adult"]
            children = request.POST["children"]
            intime = request.POST["intime"]
            indate = request.POST["indate"]
            outtime = request.POST["outtime"]
            outdate = request.POST["outdate"]
            checkin = request.POST["checkin"]
            try:
                c1 = request.POST['c1']
            except:
                c1 = 0
            try:
                c2 = request.POST['c2']
            except:
                c2 = 0
            try:
                c3 = request.POST['c3']
            except:
                c3 = 0
            try:
                c4 = request.POST['c4']
            except:
                c4 = 0
            try:
                c5 = request.POST['c5']
            except:
                c5 = 0
            pic = (request.FILES["picture"])

            obj = Checkin.objects.create(
                name=name, address=addr, id=id, age=age, gender=gender, phone=phone, email=email, checkin=checkin, pic=pic, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, adult=adult, children=children, intime=intime, indate=indate, outtime=outtime, outdate=outdate)

            msg = "Record Inserted"
            return render(request, 'result.html', {'msg': msg})

        elif button == "Select":
            id = request.POST['t1']
            obj = Checkin.objects.get(pk=id)
            return render(request, 'result.html', {'obj': obj})

        elif button == "Update":

            id = request.POST["t1"]
            name = request.POST["t2"]

            addr = request.POST["t3"]
            age = request.POST["t4"]
            gender = request.POST["gender"]
            phone = request.POST["phone"]
            email = request.POST["email"]        
            adult = request.POST["adult"]
            children = request.POST["children"]
            intime = request.POST["intime"]
            indate = request.POST["indate"]
            outtime = request.POST["outtime"]
            outdate = request.POST["outdate"]
            checkin = request.POST["checkin"]

            pic = (request.FILES["picture"])
            try:
                c1 = request.POST['c1']
            except:
                c1 = 0
            try:
                c2 = request.POST['c2']
            except:
                c2 = 0
            try:
                c3 = request.POST['c3']
            except:
                c3 = 0
            try:
                c4 = request.POST['c4']
            except:
                c4 = 0
            try:
                c5 = request.POST['c5']
            except:
                c5 = 0

            obj = Checkin.objects.get(pk=id)
            obj.name = name
            obj.address = addr
            obj.age = age
            obj.gender = gender
            obj.phone = phone
            obj.email = email
            obj.adult = adult
            obj.children = children
            obj.checkin = checkin
            obj.pic = pic
            obj.c1 = c1
            obj.c2 = c2
            obj.c3 = c3
            obj.c4 = c4
            obj.c5 = c5
            obj.save()
            msg = "Record Updated"
            return render(request, 'result.html', {'msg': msg})

        elif button == "Delete":
            id = request.POST['t1']
            obj = Checkin.objects.get(pk=id)
            obj.delete()
            msg = "Record Deleted"
            return render(request, 'result.html', {'msg': msg})
