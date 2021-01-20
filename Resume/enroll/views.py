from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#This function will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['phone']
            ct = fm.cleaned_data['city']
            bm = fm.cleaned_data['birth_date']
            xm = fm.cleaned_data['experience']
            pgm = fm.cleaned_data['programming_lang']
            cm = fm.cleaned_data['current_ctc']
            exm = fm.cleaned_data['expect_ctc']
            paas = fm.cleaned_data['password']
            reg = User(name=nm, email=em, phone=pm, city=ct, birth_date=bm, experience=xm, programming_lang=pgm, current_ctc=cm, expect_ctc=exm, password=paas)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})

# This Function Will For Edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})

#This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')