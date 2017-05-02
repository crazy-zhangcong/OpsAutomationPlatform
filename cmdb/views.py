from django.shortcuts import render

# Create your views here.


from index.views import is_login



def index(request):

    return render(request, "cmdb/index.html")
