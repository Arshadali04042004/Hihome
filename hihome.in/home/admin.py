from django.contrib import admin
from home.models import Registration,Contactus, myuploadfile
# Register your models here.

admin.site.register(Contactus)
admin.site.register(Registration)
admin.site.register(myuploadfile)