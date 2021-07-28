from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class Participant(models.Model):
    # should have a unique email address
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

 
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    # one-to-one
    # should add what is the location gets deleted-> on_delete
    # models.CASCADE -> if the related data is deleted it will also be deleted
    # models.SET_NULL -> if the related data is deleted it will be declared to NULL
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # many-to-many
    # blank=True -> Declares us that it can be left blank
    # without null=True, if blank=True, for some fields(link CharField) will return error
    participant = models.ManyToManyField(Participant, blank=True, null=True)

    orgainser_email = models.EmailField()
    date = models.DateField()


    def __str__(self):
        # This is the way the object is represented in table
        return f'{self.title} - {self.slug}'