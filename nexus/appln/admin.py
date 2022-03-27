from django.contrib import admin

# Register your models here.
from appln.models import company,contractor,job

class companyAdmin(admin.ModelAdmin):
    list_display=['cid','name','city','zipcode']

admin.site.register(company,companyAdmin)

class contractorAdmin(admin.ModelAdmin):
    list_display=['ccid','name','city','zipcode']

admin.site.register(contractor,contractorAdmin)

class jobAdmin(admin.ModelAdmin):
    list_display=['job_id','title','price','company','contractor','Date_job','time_job']

admin.site.register(job,jobAdmin)
