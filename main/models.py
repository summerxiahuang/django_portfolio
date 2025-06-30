from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag', blank=True,related_name='projects')
    description = models.TextField()
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    def get_short_message(self):
        """Return first 50 characters of the message"""
        return self.message[:50] + '...' if len(self.message) > 50 else self.message