from django.db import models


class users(models.Model):
    name = models.CharField('Event Name', max_length=120)
    email = models.EmailField(max_length = 60,unique = True)
    password = models.CharField(max_length = 60)
    db_access = models.CharField(max_length=120)
    is_admin = models.BooleanField(default= False)
    enabled = models.BooleanField(default= False)

    class Meta:
        db_table = "Users"
        

    
class projects(models.Model):    
    user_id = models.IntegerField()
    name = models.CharField(max_length=120)
    enabled = models.BooleanField(default= False)

    class Meta:
        db_table = "projects"
    