from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'var01': 11111,
        'var02': 22222,
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("hello this is About page")

def services(request):
    return HttpResponse("hello this is Services page")

