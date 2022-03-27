from django import forms
from django.db import models
from appln.models import company,contractor

class companyform(forms.Form):
    # class Meta:
    #     model=company
    #     fields='__all__'
    cid=forms.IntegerField(label='Company_ID')
    name=forms.CharField(max_length=20,label='Company_Name')
    city=forms.CharField(max_length=15,label='City')
    zipcode=forms.IntegerField(label='Zipcode')

class contractorform(forms.Form):
    # class Meta:
    #     model=contractor
    #     fields='__all__'
    cid=forms.IntegerField(label='Contractor_ID')
    name=forms.CharField(max_length=20,label='Contractor_Name')
    city=forms.CharField(max_length=15,label='City')
    zipcode=forms.IntegerField(label='Zipcode')


# class updateform(forms.Form):
#     #cid=forms.IntegerField(label='Contractor_ID')
#     name=forms.CharField(max_length=20,label='Name')
#     city=forms.CharField(max_length=15,label='City')
#     zipcode=forms.IntegerField(label='Zipcode')

# from appln.models import company,contractor
class jobform(forms.Form):
    # comp_list=company.objects.all()
    # cont_list=contractor.objects.all()
    job_id=forms.CharField(max_length=10)
    title=forms.CharField(max_length=10)
    price=forms.CharField(max_length=10)
    #favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
    company=forms.CharField(max_length=20)
    contractor=forms.CharField(max_length=20)
    date=forms.DateField()
    time=forms.TimeField()
