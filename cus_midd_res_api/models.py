# from django import models
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Job(models.Model):
    class Requirement(models.TextChoices):
        PYTHON = 'python', ('Python Developer')
        REACT = 'react', ('React Developer')
    job_name = models.CharField(max_length=105,null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    number_of_openings = models.IntegerField(null=True, blank=True)
    experience_requride = models.IntegerField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    requirement = models.CharField(max_length=12, choices=Requirement.choices, default='python')
    perks_and_benefits = models.TextField(null=True, blank=True)
    skills_required = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.job_name
    
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class CandidateDetail(BaseModel):
    email = models.EmailField(max_length=100,unique=True)
    def __str__(self) :
        return self.email
EXPERIENCE_TYPE = [
    ('fresher','Fresher'),
    ('experience','Experience')
]

class JobApply(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    # resume = models.FileField(upload_to='media')
    expected_salary = models.IntegerField(default=0)
    experience_type = models.CharField(choices=EXPERIENCE_TYPE,default='fresher',max_length=30)
    skills = models.CharField(max_length=255)
    current_salary = models.IntegerField(null=True,blank=True)
    notice_period = models.CharField(max_length=100,blank=True,null=True)
    status = models.BooleanField(default=False)
    dob = models.DateField(null=True, blank=True)
    apply_date = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.name
    
class CandidateExperience(BaseModel):
    job_apply = models.ForeignKey(JobApply,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    def __str__(self):
        return self.company_name
    
class EducationDetail(BaseModel):
    job_apply = models.ForeignKey(JobApply,on_delete=models.CASCADE)
    college_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    passout_year = models.DateField(blank=True,null=True)
    def __str__(self):
        return self.college_name