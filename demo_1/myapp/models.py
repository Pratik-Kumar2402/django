from django.db import models
    
class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    salary = models.IntegerField()
    def __str__(self):
        return self.name
    
class Section(models.Model):
    section_name = models.CharField(max_length=10)
    no_of_students = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.section_name
    
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    post = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', default='')
    def __str__(self):
        return self.title
    
class CookieDetails(models.Model):
    cookie_name = models.CharField(max_length=30)
    cookie_value = models.CharField(max_length=30)
    def __str__(self):
        return self.cookie_name