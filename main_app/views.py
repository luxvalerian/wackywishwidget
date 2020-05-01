from django.shortcuts import render, redirect
from .models import Wishes
from .forms import WishesForm

def index(request):
    wish_list = Wishes.objects.all()
    form = WishesForm()
    # context = {'wishes_list': [
    #     {'description': 'python book', 'quantity': 3}
    # ]}  
    return render(request, 'index.html', { 
        'form': form,
        'wish_list': wish_list
    })

def add_wish(request):
    form = WishesForm(request.POST)
    if form.is_valid():
        new_wish = form.save()
        new_wish.save()
    return redirect('index')
    # else:
    #     form = WishesForm()


def delete(request, wish_id):
    wish = Wishes.objects.get(id=wish_id)
    wish.delete()
    return redirect('index')
