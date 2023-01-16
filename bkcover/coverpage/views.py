from django.shortcuts import render

# Create your views here.
def cover(request):
    return render(request,"coverpage.html")

