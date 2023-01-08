from django.shortcuts import render

# Create your views here.
def cdn_method(request):
    return render(request,'cdn_method.html')