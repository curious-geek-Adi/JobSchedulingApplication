"""nexus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appln import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('compreg/',views.compview),
    path('compinfo/', views.compinfo),
    path('compdelete/<int:id>/', views.comp_delete),
    path('compupdate/<int:id>/', views.comp_update),
    path('contdelete/<int:id>/', views.cont_delete),
    path('contreg/', views.contview),
    path('continfo/',views.continfo),
    path('comp_tableinfo/',views.comp_tableinfo),
    path('cont_tableinfo/',views.cont_tableinfo),
    path('contupdate/<int:id>/', views.cont_update),
    path('jobreg/', views.jobview),
    path('jobinfo/',views.jobinfo),
    path('', views.jobview),
    path('jobupdate/<int:id>/', views.job_update),
    path('jobdelete/<int:id>/', views.job_delete),
    path('job_tableinfo/',views.job_tableinfo),
]
