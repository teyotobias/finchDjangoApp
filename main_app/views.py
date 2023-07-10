from django.shortcuts import render

finches = [
  {'name': 'Zebra Finch', 'origin': 'Australia', 'description': 'small and colorful', 'lifespan': 5},
  {'name': 'Gouldian Finch', 'origin': 'Australia', 'description': 'vibrantly colored', 'lifespan': 6},
  {'name': 'Society Finch', 'origin': 'Asia', 'description': 'friendly and social', 'lifespan': 7},
  {'name': 'Greenfinch', 'origin': 'Europe', 'description': 'greenish in color', 'lifespan': 10},
  {'name': 'Canary', 'origin': 'Canary Islands, Spain', 'description': 'renowned for their song', 'lifespan': 10},
  {'name': 'Purple Finch', 'origin': 'North America', 'description': 'rosy red or lavender', 'lifespan': 12},
  {'name': 'Chaffinch', 'origin': 'Europe', 'description': 'common and widespread', 'lifespan': 14},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request) :
    return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })