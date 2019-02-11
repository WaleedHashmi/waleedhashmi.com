from django.db import models
from datetime import datetime
from django.conf import settings

class Home(models.Model):
    title = models.CharField(max_length=20)
    resume_text = models.TextField()
    featured_projects = models.ManyToManyField('Project', blank=True)
    def __str__ (self):
         return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self) :
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True, null=True) #for the ::hover text
    body = models.TextField()
    created_at = models.DateTimeField (default=datetime.now, blank=True)
    image_main =  models.ImageField(blank=True, null=True)
    image_2 =  models.ImageField(blank=True, null=True)
    image_3 =  models.ImageField(blank=True, null=True)
    image_4 =  models.ImageField(blank=True, null=True)
    image_5 =  models.ImageField(blank=True, null=True)
    image_6 =  models.ImageField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='t1')
    top_tag_1 = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, related_name='t2')
    top_tag_2 = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, related_name='t3')
    github_link = models.CharField(max_length=100, blank=True, null=True)
    live_preview_link = models.CharField(max_length=100, blank=True, null=True)
    high_res_link = models.CharField(max_length=100, blank=True, null=True)
    Documentation_link = models.CharField(max_length=100, blank=True, null=True)
    github_link = models.CharField(max_length=100, blank=True, null=True)
    intext_image =  models.ImageField(blank=True, null=True)

    def __str__(self) :
        return self.title
