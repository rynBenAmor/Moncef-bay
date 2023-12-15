from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Item
from .forms import NewItemForm, EditItemForm


def detail(request, pk):

    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, available=True).exclude(pk=pk)[0:3]#max 3 recommmended items

    return render(request,'item/itemDetail.html',
                  {'item': item,
                   'related_items': related_items})


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)#cuz created by field is not yet added
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else: #if its a get request
        form = NewItemForm()
    return render(request,'item/form.html',
                 {'form': form,
                        'title': 'New item',})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.available = False
    item.save()
    return redirect('dashboard:index')  # Use the named URL pattern


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request,'item/form.html',
                 {'form': form, 'title': 'Edit item',})
