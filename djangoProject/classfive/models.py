from django.db import models

# Create your models here.
class event(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the \"register\" button goes to. make sure to include \"https://\" in the website address)")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class slide(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description (should be around 1-2 sentences long)")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the \"register\" button goes to. make sure to include \"https://\" in the website address)")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class card(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    date = models.TextField()
    title = models.TextField()
    desc = models.TextField(verbose_name="description (should be around 1-2 sentences long)")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the \"register\" button goes to. make sure to include \"https://\" in the website address)")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name