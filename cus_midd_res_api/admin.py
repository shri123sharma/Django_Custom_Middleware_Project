from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Job)
admin.site.register(CandidateDetail)
admin.site.register(EducationDetail)
admin.site.register(JobApply)
admin.site.register(CandidateExperience)