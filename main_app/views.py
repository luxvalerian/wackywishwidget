from django.shortcuts import render, redirect
from .models import Wishes
from .forms import WishesForm

def index(request):
    wish_list = Wishes.objects.all()
    form = WishesForm(request.POST)
    # context = {'wishes_list': [
    #     {'description': 'python book', 'quantity': 3}
    # ]}  
    # return render(request, 'index.html', context)
    if form.is_valid():
        new_wish = form.save()
        return redirect('index')
    else:
        form = WishesForm()
        wish_list = Wishes.objects.all()

    return render(request, 'index.html', { 
        'form': form,
        'wish_list': wish_list
    })

def delete(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    wish.delete()
    return redirect('index')
