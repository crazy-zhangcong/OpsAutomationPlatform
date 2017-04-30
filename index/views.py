from django.shortcuts import render

# Create your views here.


def index_func(request):

    return render(request, 'index/index.html')