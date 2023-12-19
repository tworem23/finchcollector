from django.shortcuts import render

finches = [
    {'type': 'House Finch', 'lifespan': 15, 'weight': 1},
    {'type': 'Eurasian Chaffinch', 'lifespan': 3, 'weight': 0.75}

]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })