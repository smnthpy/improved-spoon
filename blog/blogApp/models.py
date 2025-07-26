from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    staff_mem = models.BooleanField(default=False)
    profile_image = models.FileField(upload_to="profile_pic/",blank=True)
    get_full_name = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(upload_to='blogImages/',blank=True,null=True)
    slug = models.SlugField(blank=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on '{self.post.title}'"
    