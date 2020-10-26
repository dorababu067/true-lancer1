from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    groupid	= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ipaddress = models.GenericIPAddressField()
    registerdate = models.DateField(auto_now_add=True)
    last_login_date	= models.DateField(null=True, blank=True)
    created_on = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        self.username

class LoginDetails(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    type	= models.CharField(max_length=255, default='some type')
    created_on =  models.CharField(max_length=255, null=True, blank=True)	
    ipaddress = models.GenericIPAddressField(null=True, blank=True)
    useragent = models.CharField(max_length=1000)

    def  __str__(self):
        self.userid.username
