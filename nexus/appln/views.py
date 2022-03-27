from django.shortcuts import render,redirect
from appln import forms
from appln.models import company,contractor,job
# Create your views here.
def compinfo(request):
    #comp_list=company.objects.all()
    #my_dict={'comp_list':comp_list}
    return render(request,'appln/sucess.html')

def comp_update(request,id):
    comp=company.objects.get(cid=id)
    if request.method=="POST":
        comp.name=request.POST['name']
        comp.city=request.POST['city']
        comp.zipcode=request.POST['zipcode']
        comp.save()
        return redirect('/comp_tableinfo')
    return render(request,'appln/update.html',{'comp':comp})

def cont_update(request,id):
    cont=contractor.objects.get(ccid=id)
    if request.method=="POST":
        cont.name=request.POST['name']
        cont.city=request.POST['city']
        cont.zipcode=request.POST['zipcode']
        cont.save()
        return redirect('/cont_tableinfo')
    return render(request,'appln/update1.html',{'cont':cont})

def job_update(request,id):
    jo=job.objects.get(job_id=id)
    c1=company.objects.all()
    c2=contractor.objects.all()
    if request.method=="POST":
        jo.title=request.POST['title']
        jo.price=request.POST['price']
        jo.company=request.POST['company']
        jo.contractor=request.POST['contractor']
        jo.Date_job=request.POST['date']
        jo.time_job=request.POST['time']
        jo.save()
        return redirect('/job_tableinfo')
    return render(request,'appln/update2.html',{'jo':jo,'c1':c1,'c2':c2})


def job_delete(request,id):
    jo=job.objects.get(job_id=id)
    jo.delete()
    return redirect('/job_tableinfo')

def comp_tableinfo(request):
    comp_list=company.objects.all()
    #my_dict={'comp_list':comp_list}
    return render(request,'appln/info.html',{'comp_list':comp_list})

def comp_delete(request,id):
    comp=company.objects.get(cid=id)
    comp.delete()
    return redirect('/comp_tableinfo')


def cont_delete(request,id):
    cont=contractor.objects.get(ccid=id)
    cont.delete()
    return redirect('/cont_tableinfo')

def compview(request):
    form=forms.companyform()
    if request.method=='POST':
        form=forms.companyform(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            cid=form.cleaned_data['cid']
            name=form.cleaned_data['name']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            p=company(cid=cid,name=name,city=city,zipcode=zipcode)
            p.save()
            print("sucessfully store to the company Database")
            return compinfo(request)
    return render(request,'appln/register.html',{'form':form})

def continfo(request):
    #cont_list=contractor.objects.all()
    return render(request,'appln/sucess1.html')

def cont_tableinfo(request):
    cont_list=contractor.objects.all()
    return render(request,'appln/info1.html',{'cont_list':cont_list})

def contview(request):
    form=forms.contractorform()
    if request.method=="POST":
        form=forms.contractorform(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            cid=form.cleaned_data['cid']
            name=form.cleaned_data['name']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            p=contractor(ccid=cid,name=name,city=city,zipcode=zipcode)
            p.save()
            print("sucessfully stored in to contractor database")
            return continfo(request)
    return render(request,'appln/register1.html',{'form':form})



def job_tableinfo(request):
    job_list=job.objects.all()
    return render(request,'appln/info2.html',{'job_list':job_list})


def jobinfo(request):
    #comp_list=company.objects.all()
    #my_dict={'comp_list':comp_list}
    return render(request,'appln/sucess2.html')



def jobview(request):
    form=forms.jobform()
    c1=company.objects.all()
    c2=contractor.objects.all()
    jj=job.objects.all()
    if request.method=="POST":
        # form=forms.jobform(request.POST)
        # if form.is_valid():
            #form.save(commit=True)
            # job_id=form.cleaned_data['job_id']
            # title=form.cleaned_data['title']
            # price=form.cleaned_data['price']
            # comp=['company']
            # contr=form.cleaned_data['contractor']
            # date=form.cleaned_data['date']
            # time=form.cleaned_data['time']
        job_id=request.POST['id']
        title=request.POST['title']
        price=request.POST['price']
        comp=request.POST['company']
        cont=request.POST['contractor']
        Date_job=request.POST['date']
        time_job=request.POST['time']
        job.objects.create(job_id=job_id,title=title,price=price,company=comp,contractor=cont,Date_job=Date_job,time_job=time_job)
        # p.save()
        print("sucessfully stored in to contractor database")
        return jobinfo(request)
    return render(request,'appln/jobregform.html',{'c1':c1,'c2':c2})
