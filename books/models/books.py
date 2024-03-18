from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=1024, blank=True, null=True)
    gutenberg_id = models.PositiveIntegerField()
    media_type = models.CharField(max_length=16)
    download_count = models.PositiveIntegerField(default=0)
   



    

    
