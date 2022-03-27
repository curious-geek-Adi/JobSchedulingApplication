from django.db import models


# Create your models here.
class company(models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=15)
    zipcode=models.IntegerField()


class contractor(models.Model):
    ccid=models.IntegerField(verbose_name='Contractor_ID:',primary_key=True)
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=15)
    zipcode=models.IntegerField()


class job(models.Model):
    job_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    price=models.FloatField()
    company=models.CharField(max_length=20)
    contractor=models.CharField(max_length=20)
    Date_job=models.DateField()
    time_job=models.TimeField()
