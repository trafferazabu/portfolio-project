from django.db import models

# Create your models here.
# title, publication date, body, image
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=1600)
    image = models.ImageField(upload_to='images/')

    def __str__(self):  #this double underscore will reference the admin page (somehow)
        return self.title    #this is how we are getting the blog title instead of blog(1) on the admin page

    def summary(self):  #must indclude self as one of the parameters
        return self.body[:75] +"..."   #must reference self.TheItem

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
