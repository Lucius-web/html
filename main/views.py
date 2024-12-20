from django.shortcuts import render

# Create your views here.
def main(request):
  context = {
    "title": "Geeks-student"
  }

  return render(request, 'index.html', context = context)