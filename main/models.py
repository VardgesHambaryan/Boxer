from django.db import models

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
    
