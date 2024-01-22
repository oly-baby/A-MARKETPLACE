from django.shortcuts import render, redirect

from item.models import Category,item

from .forms import SignupForm 



def index(request):
    items = item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()
    return render(request, 'app/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'app/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    # form = SignupForm()
    return render(request, 'app/Signup.html', {
        'form': form
    })
    
