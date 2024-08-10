from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Home(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name_plural = 'Home'


class Divider(models.Model):
    icon = models.CharField("Icon Class Name", max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Feature(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='media')

    point1 = models.TextField('First Point Text')
    icon1 = models.CharField("Icon Class Name", max_length=255)

    point2 = models.TextField('First Point Text')
    icon2 = models.CharField("Icon Class Name", max_length=255)

    def __str__(self) -> str:
        return self.title
    
class PricingPlan(models.Model):
    name=models.CharField('Plan Name',max_length=255)
    price=models.IntegerField('Price')
    f1=models.CharField(max_length=255)
    f2=models.CharField(max_length=255)
    f3=models.CharField(max_length=255)
    f4=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
class Download(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    img=models.ImageField(upload_to='media')
    def __str__(self) -> str:
        return self.title
class ContactUs(models.Model):
    text=models.TextField()
    address=models.CharField(max_length=255)
    address_icon=models.CharField(max_length=255)
    phone1=PhoneNumberField()
    phone2=PhoneNumberField()
    phone_icon=models.CharField(max_length=255)
    email=models.EmailField()
    email_icon=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.address
    class Meta:
        verbose_name_plural="ContactUs"
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField
    def __str__(self) -> str:
        return self.name
