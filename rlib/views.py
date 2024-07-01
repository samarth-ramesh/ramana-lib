from django import forms
from django.db.models import Q
from django.forms.forms import Form
from django.http import HttpResponse
from django.shortcuts import render
from rlib.models import Book
# Create your views here.


class SearchForm(Form):
    title = forms.CharField(label="Book Title", max_length=100, required=False)
    author = forms.CharField(label="Author", max_length=100, required=False)
    category = forms.CharField(label="Category", max_length=100, required=False)


def index(request):
    if request.method == "GET":
        search_form = SearchForm()
        return render(request, "search_form.html", {"form": search_form})
    else:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            title = search_form.cleaned_data["title"]
            author = search_form.cleaned_data["author"]
            category = search_form.cleaned_data["category"]
            qobj = Q()

            if title:
                qobj |= Q(BookTitle__contains=title)
            if author:
                qobj |= Q(Author__contains=author)
            if category:
                qobj |= Q(BookCategory__contains=category)

            books = Book.objects.filter(qobj)
            return render(request, "search_form.html", {"form": search_form, "books": books})
        else:
            return HttpResponse(search_form.errors)
