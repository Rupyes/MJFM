from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


#----------news----------------------
class NewsModel(models.Model):
    NEWS_TYPES = (
    ('SPORTS','Sports News'),
    ('LOCAL','Local News'),
    ('NATIONAL','National News'),
    ('INTERNATIONAL', 'International News'),
    )

    title = models.CharField(max_length=256)
    news = models.TextField()
    src_name = models.CharField(max_length=256, null=True, blank = True, default = 'Anonymous')
    image = models.ImageField(upload_to = 'images/news_img', null=True, blank=True)
    uploaded_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField()
    newstype = models.CharField(max_length = 30, choices=NEWS_TYPES, default = 'SPORTS')
    flashNews = models.BooleanField(default=False)
    topNews = models.BooleanField(default=False)


    def __str__(self):
        return self.title



#slider
class SlideModel(models.Model):
    title = models.CharField(max_length=256)
    slide_desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'images/slides')
    uploaded_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.title


#photos and videos

class PhotosModel(models.Model):
    title = models.CharField(max_length=256, null=False)
    photo_desc = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to = 'images/gallery')
    uploaded_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class VideosModel(models.Model):
    title = models.CharField(max_length=256, null=False)
    video_desc = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='video_gallery')
    uploaded_date = models.DateTimeField(auto_now=True)
    poster = models.ImageField(upload_to='video_gallery/poster')

    def __str__(self):
        return self.title

class Day(models.Model):
    DAYS_CHOICES = (
        ('su', 'Sunday'),
        ('mo', 'Monday'),
        ('tu', 'Tuesday'),
        ('we', 'Wednesday'),
        ('th', 'Thursday'),
        ('fr', 'Friday'),
        ('sa', 'Saturday')
    )

    name_of_day = models.CharField(choices=DAYS_CHOICES, default='su', max_length=10, null=False)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name_of_day_display()

    class Meta:
        ordering = ['created_time']

class Schedule(models.Model):
    host = models.CharField(max_length=256, null=False)
    title = models.CharField(max_length=256, null=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now_add=False)
    day = models.ForeignKey('Day')

    def __str__(self):
        return self.title

class PhotoProfile(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True)
    address = models.TextField()
    profilepic = models.ImageField(upload_to='images/profiles')

    def __str__(self):
        return self.name
