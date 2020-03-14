from django.shortcuts import render
from .models import LearnMore
from .form import ContactForm
# Create your views here.
def index(request):
    return render(request,'html/myHtml.html',{})

def contactMe(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name=request.POST['name']

        return render(request, 'html/contactMe.html', {'name':name})
    else:
       return render(request,'html/contactMe.html',{})

def learnMore(request):
    data=LearnMore.objects.order_by('title')
    return render(request,'html/learnmore.html',{'data':data})




    return render(request,'html/learnmore.html',{})




