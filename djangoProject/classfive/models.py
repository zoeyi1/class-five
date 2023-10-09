from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the \"register\" button goes to. make sure to include \"https://\" in the website address)")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class Slide(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description (should be around 1-2 sentences long)")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the button goes to. make sure to include \"https://\" in the website address)")
    button = models.TextField(verbose_name="text that is in the button, for example 'register'. all caps suggested")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class Card(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    date = models.TextField()
    title = models.TextField()
    desc = models.TextField(verbose_name="description (should be around 1-2 sentences long)")
    img = models.ImageField(upload_to = "images/", verbose_name="image")
    link = models.TextField(verbose_name="link (website that the \"register\" button goes to. make sure to include \"https://\" in the website address)")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class TeamMember(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description")
    img = models.ImageField(upload_to = "images/", verbose_name="image")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name