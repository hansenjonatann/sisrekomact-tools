from django.urls import path 
from dataset import views 
urlpatterns = [
    path('' , views.home , name='home'),
    path('import_datasets/' , views.import_datasets , name='import_datasets')
]