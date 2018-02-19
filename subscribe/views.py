from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Subscriber

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_subscriber = Subscriber.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_subscriber':num_subscriber},
    )
    
class SubscriberListView(generic.ListView):
    model = Subscriber
    
class SubscriberDetailView(generic.DetailView):
    model = Subscriber
    
class SubscriberCreate(CreateView):
    model = Subscriber
    fields = '__all__'

    
