from django.db import models

# Create your models here.
class Master(models.Model):
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_verifed = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


# Model for candidate
class Candidate(models.Model):
    user_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    skills = models.CharField(max_length=150)
    contact = models.BigIntegerField(null=True, blank=True)
    h_rate = models.BigIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100 )
    about = models.CharField(max_length=1000)
    profile = models.ImageField(upload_to="app/img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    com_name = models.CharField(max_length=50)
    ceo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="app/img/company")

class job_details(models.Model):
    company_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    job_description = models.CharField(max_length=5000)
    company_information = models.CharField(max_length=5000)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    selary_packege = models.CharField(max_length=250)
    post_date = models.DateField(auto_now_add=True)
    application_date = models.DateField(auto_now_add=True)
    experience = models.IntegerField()
    company_website = models.CharField(max_length=250)
    company_email = models.EmailField(max_length=250)
    company_contact = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="app/img/JobPost",default="")

class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(job_details, on_delete=models.CASCADE)

    email = models.EmailField(max_length=200)
    protfolio = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200, default="")
    minSelary = models.CharField(max_length=200)
    maxSelary = models.CharField(max_length=200)
    cv = models.FileField(upload_to="app/img/candidate_cv")

    