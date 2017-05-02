from django.db import models

# Create your models here.


class UserProfile(models.Model):
    """
    用户信息
    """
    username = models.CharField(u'用户名', max_length=64)
    password = models.CharField(u'密码', max_length=64)

    name = models.CharField(u'姓名', max_length=32)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32, null=True, blank=True)
    mobile = models.CharField(u'手机', max_length=32)

    class Meta:
        verbose_name_plural = "用户信息表"

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    """
    用户组
    """
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField('UserProfile')

    class Meta:
        verbose_name_plural = "用户组表"

    def __str__(self):
        return self.name