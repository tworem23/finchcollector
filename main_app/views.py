from django.shortcuts import render
from .models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finch = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finch': finch
    })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {
    'finch': finch
  })