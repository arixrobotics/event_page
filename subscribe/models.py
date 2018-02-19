from django.db import models

        
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Subscriber(models.Model):
    """
    Model representing a subscriber.
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular subscriber instance.
        """
        return reverse('subscriber-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1})'.format(self.name,self.email)


        