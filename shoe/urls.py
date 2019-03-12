from django.urls import path
from .import views

# 设置命名空间名称
app_name = 'shoe'

urlpatterns = [
    path('/admin_change/',views.admin_change,name='admin_change'),
    path('/getusershoes/',views.getusershoes,name='getusershoes'),
    path('/updateusershoes/',views.updateusershoes,name='updateusershoes'),
]
