from django.shortcuts import render
from main.models import Banner
# Create your views here.

def banner(request):
  banner = Banner.objects.latest("id")
  return render(request, 'index.html', locals())

