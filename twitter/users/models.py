from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

# Custom user model inherting from the AbstractUser class built into Django
class CustomUser(AbstractUser):
    profilepicture = models.FileField(upload_to='profile_picture', default='nopic.jpeg')
    location = models.CharField(max_length=255, blank=True, default='nairobi')
    bio = models.TextField()

    def __str__(self):
        return self.username

    # Created the absolute url for a user
    # @params: username (it is unique)
    def get_absolute_url(self):
        return reverse('useroverview', kwargs={
            'username': self.username
        })
    
# class DocCustomUser(CustomUser):
#     company = models.CharField(max_length=255, blank=True)
#     website = models.URLField(max_length=255, blank=True)
#     skills = models.TextField(help_text="Comma Seperated value")
#     youtube = models.CharField(max_length=255, blank=True)
#     twitter = models.CharField(max_length=255, blank=True)
#     facebook = models.CharField(max_length=255, blank=True)
#     linkedin = models.CharField(max_length=255, blank=True)
#     instagram = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.username

# class Education(models.Model):
#     user = models.ForeignKey('DocCustomUser', on_delete=models.CASCADE, related_name='education', blank=True)
#     title = models.CharField(max_length=200)
#     company = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     from_date = models.DateField()
#     to_date = models.DateField(blank=True, null=True)
#     current = models.BooleanField(default=False)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.title
    
# class Experience(models.Model):
#     user = models.ForeignKey('DocCustomUser', on_delete=models.CASCADE, related_name='experience', blank=True)
#     school = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     field_of_study = models.CharField(max_length=255)
#     from_date = models.DateField()
#     to_date = models.DateField(blank=True, null=True)
#     current = models.BooleanField(default=False)
#     description = models.TextField(blank=True)
    
#     def __str__(self):
#         return self.school

# Follow model that keeps track of user follows
class Follow(models.Model):
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following',on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower',on_delete=models.CASCADE)
