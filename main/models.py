from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name_plural = "Home"

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
    icon1 = models.CharField('First Icon Class Name', max_length=255)

    point2 = models.TextField('Second Point Text', default='default_point_text')
    icon2 = models.CharField('Second Icon Class Name', max_length=255, default='default_icon_class')

    def __str__(self) -> str:
        return self.title
    
class Feature1(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='media')

    point1 = models.TextField('First Point Text')
    icon1 = models.CharField('First Icon Class Name', max_length=255)

    point2 = models.TextField('Second Point Text')
    icon2 = models.CharField('Second Icon Class Name', max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Features1"


class Pricing(models.Model):
    title = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    space = models.CharField(max_length=255)
    bandwidth = models.CharField(max_length=255)
    themes = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    button = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Download(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    button = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    icon1 = models.CharField(max_length=255)
    point1 = models.CharField(max_length=255)
    icon2 = models.CharField(max_length=255)
    point2 =models.CharField(max_length=255)
    icon3 = models.CharField(max_length=255)
    point3 = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    massage = models.CharField(max_length=255)
    button = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title







