from django.shortcuts import render


# Create your views here.
def portofolio(request):
    
    return render(request, "portofolio/porfolio.html")