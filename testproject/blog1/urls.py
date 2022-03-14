from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$', views.admin_reg, name='admin_reg'),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^admin_log$', views.admin_log, name='admin_log'),
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^company_reg$', views.company_reg, name='company_reg'),
    re_path(r'^company_save$', views.company_save, name='company_save'),
    re_path(r'^branch_reg$', views.branch_reg, name='branch_reg'),
    re_path(r'^logout$', views.logout, name='logout'),
]
              
