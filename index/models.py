from django.db import models

choices=[('Available',True),('Issued',False)]

class Books(models.Model):
    bid=models.AutoField(primary_key=True)
    btitle=models.CharField(max_length=30,blank=False,null=False,unique=True)
    author=models.CharField(max_length=30,blank=True)
    status=models.CharField(max_length=10,choices=choices,default='Available')
    user=models.CharField(max_length=30,null=False,blank=True)
    date=models.DateField(blank=True)
    fine=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.bid