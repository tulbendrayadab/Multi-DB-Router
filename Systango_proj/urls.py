
from django.contrib import admin
#from django.urls import path
from django.conf.urls import include, url
# from Users.views import SaveUser,get_user,register

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('Users.urls', namespace='Users')),
    # url(r'user/SaveUser', SaveUser,name='saveuser'),
    # url(r'user/get_user', get_user,name='get_user'),
    # url(r'user/register', register,name='get_user'),
     
]
