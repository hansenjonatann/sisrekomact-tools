from django.shortcuts import render , redirect 
from django.core.management import call_command 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request , template_name='mahasiswa/home.html')


def import_datasets (request):
    if request.method == 'POST' :
        try: 
            call_command('importdataset')
            messages.success(request , 'Successfully imported datasets')
        except Exception as e:
            messages.error(request , f'Error importing students : {e}')
        return redirect('/')
    else : 
        return redirect('/')