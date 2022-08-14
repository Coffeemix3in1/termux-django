from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
def index(request):
    """The home page for djangoapp."""

    return render(request,'djangoapp/index.html')


