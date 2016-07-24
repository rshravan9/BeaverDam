from django.db import models
from django.contrib.staticfiles import finders


class Video(models.Model):
    annotation = models.TextField(blank=True)
    source = models.CharField(max_length=1048, blank=True)
    filename = models.CharField(max_length=100, blank=True, unique=True)
    host = models.CharField(max_length=1048, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return '/video/{}'.format(self.id)

    @property
    def url(self):
        if finders.find('videos/{}.mp4'.format(self.id)):
            return '/static/videos/{}.mp4'.format(self.id)
        elif not (self.filename and self.host):
            raise Exception('Video {0} does not have a filename or host. Possible fixes: \n1) Place {0}.mp4 into static/videos to serve locally. \n2) Update the filename & host fields of the Video with id={0}'.format(self.id))
        else:
            return self.host + self.filename
