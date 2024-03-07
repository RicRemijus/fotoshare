from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images':images})


