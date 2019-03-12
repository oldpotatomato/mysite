from django.db import models

#用户信息
class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20,blank=False,unique=True,null=False)
    shoesnum = models.IntegerField(blank=False,null=False)
    is_valid_choices = (
        (0, '无效'),
        (1, '有效'),
    )
    isValid = models.IntegerField(db_column='is_valid', choices=is_valid_choices, default=1)

#鞋子信息
class Shoes(models.Model):
    shoesid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete="CASCADE")
    color = models.CharField(max_length=10,null=False)
    size = models.IntegerField(null=False)
