from django.forms import ModelForm
from .models import users,projects
from django import forms

# class project_form(ModelForm):
#     class Meta: 
#         model = projects 
#         fields = ['name']   

        
class user_form(forms.Form):  
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    OPTIONS = (
            ("database1", "Database1"),
            ("database2", "Database2"),
            ("database3", "Database3"),
            ("database4", "Database4"),
            ("database5", "Database5"),
            )
    db_choices = forms.MultipleChoiceField(choices=OPTIONS,widget=forms.CheckboxSelectMultiple)
        
        
class project_form(forms.Form):  
    name = forms.CharField(max_length=60)
    
    # user_db = users.objects.get(pk=3)
    # db_access =list( user_db.db_access.split(';'))
    # OPTIONS  = tuple([tuple([x,x]) for x in db_access])
    OPTIONS = (
            ("database1", "Database1"),
            ("database2", "Database2"),
            ("database3", "Database3"),
            ("database4", "Database4"),
            ("database5", "Database5"),
            )
    db_choices = forms.MultipleChoiceField(choices=OPTIONS,widget=forms.CheckboxSelectMultiple)
    # db_choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
        
class signin_form(forms.Form):  
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

        

    
       