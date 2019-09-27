from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class  userProfile(models.Model):
    USER = models.OneToOneField(User, on_delete = models.CASCADE,null= False)
    hobbies = models.CharField(max_length = 255,null=True ,blank = True)
    selfIntroduction = models.TextField(null=True ,blank = True)
    def __str__(self):
        return self.USER.username


class userArticle(models.Model):
    id = models.AutoField(primary_key=True)
    USER = models.ForeignKey(User, on_delete = models.CASCADE,null= True)
    Article_title = models.CharField(max_length = 255,null=True ,blank = True)
    Article = models.TextField(null=True,blank = True)
    def __str__(self):
        return self.USER.username