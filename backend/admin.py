
# Register your models here.
from django.contrib import admin
#from .models import Patient, Test
from backend.models import Patient, Test,LabHeadSignup,PatientSignup, LabTest

# admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Test)

admin.site.register(LabHeadSignup)
admin.site.register(PatientSignup)
admin.site.register(LabTest)
