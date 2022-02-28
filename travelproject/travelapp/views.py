from django.shortcuts import render
from . models import place
from . models import people

# Create your views here.
def demo(request):
    obj = place.objects.all()
    peo = people.objects.all()
    return render(request,"index.html",{"result":obj,"result1":peo})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     plus=x+y
#     ress=x-y
#     mul=x*y
#     divv=x/y
#     return render(request,"result.html",{'result':plus,'result1':ress,'result2':mul,'result3':divv})
#
#
#
#
#
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("thirdd page")