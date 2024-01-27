from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect


from .forms import NewItemForm, EditItemForm
from .models import Category, item

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    categories = Category.objects.all()
    items = item.objects.filter(is_sold=False)
    
    
    if category_id:
        items = items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q (name_icontains=query) | Q(description_icontains=query) )
    
    return render(request, 'item/items.html',{
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

 

def details(request, pk):
    items = get_object_or_404(item, pk=pk)
    related_items = item.objects.get(id = pk)
    
    return render(request, 'item/details.html', {
        'items': items,
        'related_items': related_items
    })
@login_required   
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        
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
@login_required   
def edit(request, pk):
    item = get_object_or_404(item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        
        if form.is_valid():
            item.save()
            
            return redirect('item:details', pk=item.id)
    else:    
     form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
        
    })
    
@login_required
def delete(request, pk):
    item = get_object_or_404(item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')
    
    
    
