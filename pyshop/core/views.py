from django.shortcuts import render,redirect, get_object_or_404

from .forms import SignupForm
from item.models import Category, Item

# Create your views here.
#then create urls directory



def index(request):
    items = Item.objects.filter(available=True)
    categories = Category.objects.all()

    return render(request,'core/index.html',
                  {'categories':categories,
                           'items':items,} )



def contact(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/contact.html', {'email': item.created_by.email})


def signup(request):
    if request.method == 'POST':
        form = (SignupForm(request.POST))

        if form.is_valid():
            form.save()
            return redirect('core:login')


    else:
        form = SignupForm()# created in forms.py

    return render(request, 'core/signup.html',
                  {'form': form})#then to signup html