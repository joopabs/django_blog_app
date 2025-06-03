from django.http import JsonResponse
from django.urls import path
from . import views


def chrome_devtools_json(request):
    # Return an empty JSON response
    return JsonResponse({})


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    # Add this line to handle the Chrome DevTools request
    path(".well-known/appspecific/com.chrome.devtools.json", chrome_devtools_json),
]
