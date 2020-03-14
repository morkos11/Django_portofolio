from django.db import models

class ContactMe(models.Model):
    name=models.CharField(max_length=125)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name


class LearnMore(models.Model):
    title=models.CharField(max_length=125)
    note=models.TextField()
    url=models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_pics/images',blank=True,)


    def __str__(self):
        return self.title