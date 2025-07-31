"""156p"""
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True) #괄호안에 auto_now_add=True 추가

    updated_at = models.DateTimeField(auto_now_add=True, null=True) #해당줄추가
    # author : 추후작성예정

    def __str__(self):
        return f' [ {self.pk} ]{self.title}'



"""

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True) #(auto_now=True, null=True)
    #updated_date = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'게시글제목 : {self.title} - 게시글내용 - {self.content}'

"""