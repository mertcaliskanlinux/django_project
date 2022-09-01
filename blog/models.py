
from django.db import models


class Account(models.Model):
    image = models.ImageField(verbose_name="image")
    name = models.CharField(verbose_name="name",max_length=25)
    surname = models.CharField(verbose_name="surname",max_length=30)
    description = models.TextField(verbose_name="account_description",max_length=500)
    linked = models.URLField(verbose_name="linked")
    twitter = models.URLField(verbose_name="twitter")
    github = models.URLField(verbose_name="github")

    def __str__(self):
        return self.name



class Welcome(models.Model):
    title = models.CharField(verbose_name="welcome-title",max_length=50)
    description = models.TextField(verbose_name="welcome_description",max_length=500)
    pdf = models.FileField(upload_to='static/blog-static/pdf',blank=True)
    
    def __str__(self):
        return self.title

class Skılls(models.Model):
    title = models.CharField(verbose_name="skill_title",max_length=50)
    count_bar = models.IntegerField(verbose_name="count_bar")

    def __str__(self):
        return self.title

class Expertise(models.Model):
    title1 = models.CharField(max_length=100,blank=True)
    title2 = models.CharField(max_length=100,blank=True)

    def __str__(self):
        self.title3 = f"{self.title1} --- {self.title2}"
        return self.title3

class Business_Areas(models.Model):
    title = models.CharField(verbose_name="business-title",max_length=50)
    description = models.TextField(verbose_name="business-description",max_length=200)
    
    def __str__(self):
        return self.title


class Certifica(models.Model):
    title = models.CharField(verbose_name="certifica-title",max_length=50)
    description = models.TextField(verbose_name="certifica-description",max_length=300)
    year = models.IntegerField(verbose_name="year")

    def __str__(self):
        return self.title


class Scholl(models.Model):
    title = models.CharField(verbose_name="scholl-title",max_length=100)
    description = models.TextField(verbose_name="scholl-description",max_length=200)
    year_duration = models.CharField(verbose_name="scholl-duration",max_length=20)

    def __str__(self):
        return self.title

class Interests(models.Model):
    pngimage = models.ImageField(upload_to="icon/",verbose_name="İcon PNG",blank = True)
    title = models.CharField(verbose_name="ınterests-title",max_length=50)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    year_duration = models.CharField(verbose_name="experience-duration",max_length=20)
    title = models.CharField(verbose_name="experience-title",max_length=100)
    description = models.TextField(verbose_name="experience-description",max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255 ,verbose_name="Blog Title")
    blogurl = models.URLField(verbose_name="url-title")
    image = models.ImageField(verbose_name="blog-images")

    def __str__(self):
        return self.title



