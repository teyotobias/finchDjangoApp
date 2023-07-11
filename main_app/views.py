from django.shortcuts import render

from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'

class FinchUpdate(UpdateView):
   model = Finch
   fields = ['origin', 'description', 'lifespan']

class FinchDelete(DeleteView):
   model = Finch
   success_url = '/finches'

def home(request):
    return render(request, 'home.html')


def about(request) :
    return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html',{
     'finches': finches
  })

def finches_detail(request, finch_id):
   requestedfinch = Finch.objects.get(id=finch_id)
   return render(request, 'finches/detail.html', {'finch': requestedfinch})