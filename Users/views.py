from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import users,projects
from django.views import generic
import random
import string
import json
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import user_form,project_form,signin_form


#**************    User Login / Registration BEGIN             *********************#
# Send email just after the user register
def send_email(email,message=""):
    email_from = settings.EMAIL_HOST_USER
    subject, from_email, to = 'Your password for django app', email_from, email
    text_content = 'This is an important message.'
    html_content = message
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# Register the user
def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html',{'form':form})


# Login the user and redirect to admin/user home
def user_login(request):
    if request.method =='POST':
        form = signin_form(request.POST)
       
        if form.is_valid():                  
           
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
  
            user = users.objects.get(email__iexact=email,password__iexact = passwd)
            request.session['user_id'] = user.id
       
            if user.is_admin:
                return redirect( '/admin_dashboard/'+str(user.id)+'/')
            return redirect( '/get_user/'+str(user.id)+'/')        
    else:
        form = signin_form()
    return render(request, 'user/signin.html',{'form':form})


#**************    User Login / Registration End             *********************#


#**************    Admin Section BEGIN            *********************#


def admin_dashboard(request,id):
    urs = users.objects.filter(enabled=1,is_admin=0)
    return render(request, 'admin_home.html',{'users':urs})

def edit_user(request,id):

    if request.method=='POST':
        form = user_form(request.POST)
        
        name = form.cleaned_data['name']          
        db_choices = form.cleaned_data['db_choices']
        db_choice = ';'.join(db_choices)

        user = users.objects.get(id=id)
        user.name =name
        user.db_access = db_choice
        
        user.save()


        login_user_id =request.session['user_id']
        urs = users.objects.filter(id =login_user_id)            
        return redirect( '/admin_dashboard/'+str(login_user_id)+'/')

    else:
        all_db = ['database1','database2','database3','database4','database5',]
        db_list = []
        user = users.objects.get(pk=id)    
        db_access =list( user.db_access.split(';'))
        idx = 0
        for db in all_db:
            exist_db = [True for d in db_access if d==db]

            if not exist_db:
                db_list.append([db,False,idx])
            else:
                db_list.append([db,True,idx])
            idx = idx + 1
        
        return render(request, 'edit_user.html',{'users_name':user.name,'databases': db_list})

def user_delete(request,id):
 
    user = users.objects.get(id=id)
    user.delete()
    login_user_id =request.session['user_id']
    urs = users.objects.filter(id =login_user_id)            
    return redirect( '/admin_dashboard/'+str(login_user_id)+'/')
       


def user_register(request):
    if request.method =='POST':

        form = user_form(request.POST)
       
        if form.is_valid():
            user = users()           
            user.name =form.cleaned_data['name']     
            user.email = form.cleaned_data['email']
            db_choices = form.cleaned_data['db_choices']
            user.db_access = ';'.join(db_choices)
            user.is_admin = False
            user.enabled = True
            passwd = randomString()
            user.password = passwd
            user.save()
            html_message = "<html><body>Please login using below credentials:<br/> <b>UserName: "+form.cleaned_data['email']+"<br/> Password: "+passwd+"<b>  <body></html>"
            send_email( form.cleaned_data['email'],message=html_message)

            urs = users.objects.filter(enabled=1,is_admin=0)
            return render(request, 'admin_home.html',{'users':urs})
            
    else:
        form = user_form()
    return render(request, 'register_user.html',{'form':form})


def randomString(stringLength=8):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))




#**************    Admin Section END            *********************#


#**************    User Section BEGIN            *********************#

def add_projects(request):
    if request.method =='POST':

        form = project_form(request.POST)
       
        if form.is_valid():
            db_choices = form.cleaned_data['db_choices']
            databases = ""
            
            
            project = projects()           
            project.name =form.cleaned_data['name']                 
            project.user_id = request.session['user_id']
            project.enabled =True  
            for db_choice in db_choices:
                databases = databases+" "+db_choice
              
                if db_choice=='database3': 
                    project.save()    
                else:  
                    project.save(using=db_choice)
            if databases == "":
                databases = "None"
            return redirect( '/get_user/'+str(request.session['user_id'])+'/')
            
    else:
        form = project_form()
        user_id = request.session['user_id']
       
        user = users.objects.get(pk=user_id)
        db_access =list( user.db_access.split(';'))
        form.fields['db_choices'].choices  = [(title, title) for title in db_access]
        
    return render(request, 'create_project.html',{'form':form,'id':id})



def edit_project(request,id,instance):
    p = projects()
    project = projects.objects.using(instance).filter(id = id,enabled =1).first()
    return render(request, 'edit_project.html',{'project':project,'instance':instance})
    
def update_project(request,id,instance):
    if request.method=='POST':
      
        proj = projects.objects.using(instance).get(id=id)
        user_id = proj.user_id
        proj.name = request.POST.get('name')
        proj.save(using=instance)
        return redirect( '/get_user/'+str(user_id)+'/')
        
    return render(request, 'detail_user.html',{'project':project,'instance':instance})

def delete_project(request,id,instance):
    
    proj = projects.objects.using(instance).get(id=id)
    user_id = proj.user_id
    proj.delete(using=instance)
    return redirect( '/get_user/'+str(user_id)+'/')
        


def get_user(request,id):
    
    u = users.objects.get(pk=id)    
    db_access =list( u.db_access.split(';'))
    project_list = []
    p_name = []
    dictn_project = {}
    for db in db_access:
        try:  
            if db =='database3':
                db = 'default'
            project = projects.objects.using(db).filter(user_id = id,enabled =1)
            
            title = []
            for p in project:
                project_list.append([p.name,db,p.id])

        except Exception as ex: 
            print(ex) 
            pass
    return render(request, 'user_home.html',{'list_proj':project_list,'user_db':db_access,'user':u})

#**************    User Section END            *********************#