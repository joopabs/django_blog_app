from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def posts(request):
    return HttpResponse("Hello, world. You're at the posts page.")


def post_detail(request):
    return HttpResponse("Hello, world. You're at the post detail page.")
