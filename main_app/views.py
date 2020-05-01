from django.shortcuts import render

def index(request):
    context = {'widget_list': [
        {'description': 'python book', 'quantity': 3}
    ]}
    return render(request, 'index.html', context)
