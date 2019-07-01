from django.conf.urls import include, url
from .views import user_register,get_user,add_projects,user_login,update_project,delete_project
from . import views
app_name = 'Users'
urlpatterns = [
    url(r'^$',  user_login,name='signin'),
    url(r'^user_register', user_register,name='user_register'),
    url(r'^signin', user_login,name='signin'),
    url(r'^get_user/(?P<id>[0-9]+)/', get_user,name='get_user'),
    url(r'^edit_project/(?P<id>[0-9]+)/(?P<instance>[\w.@+-]+)/', views.edit_project,name='edit_project'),
    url(r'^update_project/(?P<id>[0-9]+)/(?P<instance>[\w.@+-]+)/', update_project,name='update_project'),
    url(r'^delete_project/(?P<id>[0-9]+)/(?P<instance>[\w.@+-]+)/', delete_project,name='delete_project'),
    # url(r'^add_projects/(?P<id>[0-9]+)/', add_projects,name='add_projects'),
    url(r'^add_projects/', add_projects,name='add_projects'),
    url(r'^admin_dashboard/(?P<id>[0-9]+)/', views.admin_dashboard,name='admin_dashboard'),
    url(r'^edit_user/(?P<id>[0-9]+)/', views.edit_user,name='edit_user'),
     url(r'^delete_user/(?P<id>[0-9]+)/', views.user_delete,name='edit_user'),
]
