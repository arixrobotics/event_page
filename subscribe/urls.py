from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribers/', views.SubscriberListView.as_view(), name='subscribers'),
    path('subscriber/<int:pk>', views.SubscriberDetailView.as_view(), name='subscriber-detail'),
    path('subscriber/create/', views.SubscriberCreate.as_view(), name='subscriber_create'),
]
