from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .forms import NewItemForm
from .models import item

# Create your views here.def 

def details(request, pk):
    items = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(category=item.category, is_sold = False ).exclude(pk=pk)[0:6]
    
    return render(request, 'item/details.html', {
        'items': items,
        'related_items': related_items
    })
@login_required   
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILFS)
        
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:details', pk=item.id)
    else:    
     form = NewItemForm()
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })
    
    
    
