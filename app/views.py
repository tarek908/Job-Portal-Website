from django.shortcuts import render, redirect
from .models import *
from random import randint

# Create your views here.
# View for index page
def index(request):
    return render(request, "app/index.html")


# View for signup page
def signupPage(request):
    return render(request, "app/signup.html")


# View for login page
def loginPage(request):
    return render(request, "app/login.html")


# view for register
def register(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        user = Master.objects.filter(email=email)

        if user:
            message = "user alrady exist."
            return render(request, "app/login.html", {'msg':message})

        else:
            if password == c_password:
                otp = randint(100000,999999)
                new_user = Master.objects.create(role=role, otp=otp, email=email, password=password)

                new_candidate = Candidate.objects.create(user_id=new_user, name=name)
                return render(request, "app/otpverify.html",{'email':email})

            else:
                message = "password dose not matched."
                return render(request, "app/signup.html", {'msg':message})
    else:
        # print("company register")
        if request.POST['role']=="Company":
            role = request.POST['role']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            c_password = request.POST['c_password']


            user = Master.objects.filter(email=email)

            if user:
                message = "user alrady exist."
                return render(request, "app/login.html",{'msg':message})
            else:
                if password == c_password:
                    otp = randint(100000,999999)

                    new_user = Master.objects.create(role=role, otp=otp, email=email, password=password)

                    new_com = Company.objects.create(user_id=new_user, ceo=name)
                    
                    message = "Register Successfully."
                    return render(request, "app/otpverify.html", {'email': email})

                else:
                    message = "confirm password dose not matched."
                    return render(request, "app/signup.html", {'msg':message})
        else:
            message = "Please select a role"
            return render(request, "app/signup.html",{'msg':message})


# // Login user
def LoginUser(request):
    if request.POST['role']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user = Master.objects.get(email=email)
        if user:
            if user.password == password and user.role == "Candidate":

                can = Candidate.objects.get(user_id=user)

                request.session['id'] = user.id
                request.session['email'] = user.email
                request.session['role'] = user.role
                request.session['name'] = can.name
                return redirect('index')

            else:
                message = "Password did not matched."
                return render(request, "app/login.html", {'msg':message})
        else:
            message = "user dose not exist."
            return render(request, "app/signup.html", {'msg':message})
    else:
        if request.POST['role']=="Company":
            email = request.POST['email']
            password = request.POST['password']

            user = Master.objects.get(email=email)
            if user:
                if user.password == password and user.role == "Company":
                    com = Company.objects.get(user_id=user)

                    request.session['role'] = user.role
                    request.session['id'] = user.id
                    request.session['user_id'] = user.id
                    request.session['name'] = com.ceo
                    request.session['email'] = user.email
                    request.session['password'] = user.password

                    return redirect('deshbord')

                else:
                    message = "passwor dose not matched"
                    return render(request, "app/login.html", {'msg':message})

            else:
                message = "company dose not exist"
                return render(request, "app/signup.html", {'msg':message})
        else:
            message = "please select a role"
            return render(request, "app/signup.html", {'msg':message})

# // view for profile page 
def profile(request, pk):

    user = Master.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)


    return render(request, "app/profile.html", {'user':user,'can':can,'pk':pk})


# // profile update
def profileUpdate(request, pk):
    user = Master.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)

        can.name = request.POST.get('name')
        can.title = request.POST.get('title')
        can.skills = request.POST.get('skills')
        can.contact = request.POST.get('contact')
        can.h_rate = request.POST.get('h_rate')
        can.city = request.POST.get('city')
        can.address = request.POST.get('address')
        can.dob = request.POST.get('dob')
        can.gender = request.POST.get('gender')
        can.about = request.POST.get('about')
        
        can.save()
        url = f'/profile/{pk}'
        return redirect(url)

#// profile image update
def profielImage(request, pk):

    user = Master.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        if request.method == "POST":

            can.profile = request.FILES.get('profile')

            can.save()
            url = f'/profile/{pk}'
            return redirect(url)






# // OTP verifications
def otpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = Master.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "OTP Right."
            return render(request, "app/login.html", {'msg':message})
    
        else:
            message="otp dose not matched."
            return render(request, "app/otpverify.html", {'msg':message})

    else:
        message="email dose not matched."
        return render(request, "app/otpverify.html", {'msg':message})



#// apply page
def applyPage(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = job_details.objects.get(id=pk)
    return render(request, "app/apply.html",{'user':user,'can':can,'job':job})

#// apply sbmit view
def ApplyJob(request, pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = job_details.objects.get(id=pk)

        education = request.POST['education']
        minselary = request.POST['minselary']
        maxselary = request.POST['maxselary']
        protfolio = request.POST['protfolio']
        experience = request.POST['experience']
        cv = request.FILES['cv']

        newApply = ApplyList.objects.create(
                                            candidate=can,
                                            job=job,
                                            education=education,
                                            minSelary=minselary,
                                            maxSelary=maxselary,
                                            protfolio=protfolio,
                                            experience=experience,
                                            cv=cv,
                                         )
        message="Job applyed successfully."
        return render(request, "app/apply.html", {'msg':message})
        

################------ Company  -----#############

# // views for company deshbord
def CompanyDeshbord(request):
    return render(request, "app/company/index.html")

# // view for company profile
def comProfile(request, pk):
    user = Master.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request, "app/company/register.html",{'user':user,'comp':comp})

#// view for company pro update 
def comUpdate(request, pk):
    user = Master.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        
        comp.ceo = request.POST['ceo']
        comp.com_name = request.POST['com_name']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.logo = request.FILES['logo']

        comp.save()
        url = "/comProfile/{pk}/"
        return redirect(url)

#// view for jobpost page
def jobPostPage(request, pk):
    return render(request, "app/company/jobpost.html")

# // view for post a job
def jobDetails(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        return redirect('login')
    
    user = Master.objects.get(id=user_id)

    if user.role == "Company":
        comp = Company.objects.get(user_id=user)

        jobname = request.POST['jobname']
        company_name = request.POST['company_name']
        job_description = request.POST['job_description']
        company_information = request.POST['company_information']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        selary_packege = request.POST['selary_packege']
        experience = request.POST['experience']
        company_website = request.POST['company_website']
        company_email = request.POST['company_email']
        company_contact = request.POST['company_contact']
        logo = request.FILES['logo']

        newJob = job_details.objects.create(
            company_id=user,
            jobname=jobname,
            company_name=company_name,
            job_description=job_description,
            company_information=company_information,
            qualification=qualification,
            responsibilities=responsibilities,
            location=location,
            selary_packege=selary_packege,
            experience=experience,
            company_website=company_website,
            company_email=company_email,
            company_contact=company_contact,
            logo=logo,
        )
        
        message ="Job posted successfully"
        return render(request, "app/company/index.html",{'msg':message})


#// view for job table
def job_table(request):
    all_job = job_details.objects.all()
    return render(request, "app/company/jobtables.html",{'all_job':all_job})

#// view for can job list
def can_job_table(request):
    all_job = job_details.objects.all()
    return render(request, "app/job_listing.html",{'all_job':all_job})

#// apply list
def JobApplyList(request):
    all_jobapply = ApplyList.objects.all()
    return render(request, "app/company/applyJobList.html", {'all_job':all_jobapply})


#// company logout
def companylogout(request):
    if 'email' in request.session:
        del request.session['email']
    if 'password' in request.session: 
        del request.session['password']

    request.session.flush()

    return render(request, "app/index.html")


#// Candidate logout
def Candidatelogout(request):
    if 'email' in request.session:
        del request.session['email']
    if 'password' in request.session: 
        del request.session['password']

    request.session.flush()

    return render(request, "app/index.html")



#### ---- Admin pannel ----########

def adminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request, "app/admin/index.html")
    else:
        return redirect('adminloginpage')
    return render(request, "app/admin/index.html")

# // admin pannel
def AdminLoginPage(request):
    return render(request, "app/admin/login.html")

def adminLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password

        return redirect('adminindex')

    else:
        message = "passwor and user not matched."
        return render(request, "app/admin/login.html",{'msg':message})

def UserList(request):
    all_user = Master.objects.filter(role="Candidate")
    return render(request, "app/admin/UserList.html", {'all_user':all_user})

def UserDelete(request, pk):
    user = Master.objects.get(pk=pk)
    user.delete()
    return redirect('userList')


def CompanyList(request):
    all_Company = Master.objects.filter(role="Company")
    return render(request, "app/admin/CompanyList.html", {'all_Company':all_Company})

def VerifiedCompany(request, pk):
    com = Master.objects.get(pk=pk)
    if com:
        return render(request,"app/admin/verified.html",{'com':com})

def Verified(request,pk):
    com = Master.objects.get(pk=pk)
    if com:
        com.is_verifed = request.POST['role']
        com.save()
        return redirect('companyList')

def CompanyDelete(request, pk):
    com = Master.objects.get(pk=pk)
    com.delete()
    return redirect('companyList')


    






########### About sectiion ###########
def AboutPage(request):
    return render(request, "app/about.html")















# AI soliution
"""
def jobDetails(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # যদি ইউজার লগইন না করে থাকেন অথবা সেশনে আইডি না থাকে
        return redirect('login')  # লগইন পেজে রিডিরেক্ট করুন

    user = Master.objects.get(id=user_id)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)

        # আপনার কাজের বিবরণ সংরক্ষণের লজিক এখানে
        jobname = request.POST['jobname']
        company_name = request.POST['company_name']
        job_description = request.POST['job_description']
        company_information = request.POST['company_information']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        selary_packege = request.POST['selary_packege']
        experience = request.POST['experience']
        company_website = request.POST['company_website']
        company_email = request.POST['company_email']
        company_contact = request.POST['company_contact']

        newJob = job_details.objects.create(
            company_id=user, 
            jobname=jobname, 
            company_name=company_name, 
            job_description=job_description, 
            company_information=company_information, 
            qualification=qualification, 
            responsibilities=responsibilities, 
            location=location, 
            selary_packege=selary_packege, 
            experience=experience, 
            company_website=company_website, 
            company_email=company_email, 
            company_contact=company_contact
        )

        message = "Job posted successfully."
        return render(request, "app/company/jobpost.html", {'msg': message})

"""

# # view for signup
# def signup(request):
#     if request.method == "POST":
#         role = request.POST.get('role')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         c_password = request.POST.get('c_password')

#         user = Master.objects.filter(email=email).first()

#         if user:
#             message = "User alrady exist"
#             return render(request, "app/login.html",{'msg':message})

#         if c_password == password:
#             message = "Congo"
#             return render(request, "app/otpverify.html",{'msg':message})

#         else:
#             message = "password dose not matched"
#             return render(request, "app/signup.html",{'msg':message})

#         otp = randint(100000,999999)
#         new_user = Master.objects.create(role=role, email=email, password=password, otp=otp)

#         if role == "cndidate":
#             Candidate.objects.create(user_id=new_user, name=name)

#         if role == "company":
#             Company.objects.create(user_id=new_user, com_nam=name)

#         return render(request, "app/otpverify.html")

#     return render(request, "app/signup.html")

# # View for otp verify
# def otpVerify(request):
#     email = request.POST.get('email')
#     otp = int(request.POST.get('otp'))

#     user = Master.objects.filter(email=email).first()
#     if otp == user.otp:
#         return render(request, "app/login.html")
#     else:
#         message = "OTP dose not matched."
#         return render(request, "app/otpverify.html",{'msg':message})