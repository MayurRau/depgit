from django.shortcuts import render

# Create your views here.


def func(r):
    return render(r, 'dep/index.html')
