from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
from datetime import datetime


def post_featured_image_upload_path(instance, filename):
    # Get the current publication date of the post
    publication_date = instance.post_date
    # Get the year, month, and day from the publication date
    year = publication_date.year
    month = publication_date.month
    day = publication_date.day
    # Create the path to the folder using the year/month/day structure
    folder_path = f"post-featured-images/{year}/{month}/{day}"
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    # Return the full file path including the filename
    return os.path.join(folder_path, filename)

# Post model
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    post_excerpt = models.TextField(default=" brief summary")
    featured_image = models.FileField(upload_to='post_featured_image_upload_path')
    tags = models.ManyToManyField('Tag', blank=True)   
    
    def __str__(self):
        return self.post_title

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# comment tag
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text


    
    
