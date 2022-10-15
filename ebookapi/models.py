from django.db import models
from django.contrib.auth.models import User



class Books(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    favourite=models.BooleanField()
    options=[
        ("fantasy","fantasy"),
        ("literary","literary"),
        ("mystery","mystery"),
        ("non-fiction","non-fiction"),
        ("science-fiction","science-fiction"),
        ("thriller","thriller")
    ]
    genre=models.CharField(max_length=200,choices=options,default="")

    def __str__(self):
        return self.title
class Review(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)



# Create your models here.
