import re
from django.shortcuts import render, redirect
from .models import Review
# Create your views here.

def index(request):
    review = Review.objects.all()
    context = {
        'review': review
    }
    return render(request, 'articles/index.html', context)

def create(request):
    return render(request, 'articles/create.html')

def detail(request, reviewpk):
    review = Review.objects.get(pk=reviewpk)
    context = {
        'review': review
    }
    return render(request,'articles/detail.html',context)

def new(request):
    newname = request.GET.get('namecreate')
    newtext = request.GET.get('textcreate')
    Review.objects.create(title=newname, content=newtext)
    return redirect("articles:index")

def edit(request, reviewpk):
    review = Review.objects.get(pk=reviewpk)
    context = {
        "review": review
    }
    return render(request, 'articles/edit.html', context)

def update(request, reviewpk):
    review = Review.objects.get(pk=reviewpk)
    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content
    review.save()
    return redirect("articles:index")

def delete(request, reviewpk):
    review = Review.objects.get(pk=reviewpk)
    review.delete()
    return redirect("articles:index")