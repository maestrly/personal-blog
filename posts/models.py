from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    
    def __str__(self):
        return self.title
        
    #Create function to make pub date on webpage show only the mon, date, year
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
     
    #Return only the first 100 characters of the body so that it does not
    #show the entire body.
    def summary(self):
        return self.body[:100]