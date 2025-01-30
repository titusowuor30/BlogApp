from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=255)
    introduction=models.TextField()
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}- {self.author}'
    
    
    class Meta:
        ordering=['-date_added']

        

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)






