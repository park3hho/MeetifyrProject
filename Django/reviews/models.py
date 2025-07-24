from django.db import models
from common.models import CommonModel
# Create your models here.
class Review(models.Model):  
    content = models.CharField(max_length= 100)
    likes = models.PositiveBigIntegerField(default=0)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE) 
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)
