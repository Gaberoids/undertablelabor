from django.shortcuts import render

def index(request):
    print(" request below ---------***********-----------------**************------------")
    print(request)
    print(" request END ---------***********-----------------**************------------")

    return render(request, "home/index.html")
