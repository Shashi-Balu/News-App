from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark
API_KEY = 'f53b76be9a034f149f44636967aa99ab' 

@login_required
def home(request):
    default_url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    default_response = requests.get(default_url)
    default_data = default_response.json()
    default_articles = default_data['articles']
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        # Fetch top headlines based on user-selected country
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        # Fetch top headlines based on user-selected category
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        # If no country or category is specified, use default articles
        articles = default_articles

    context = {
        'articles': articles
    }
    return render(request, 'news_api/home.html', context)

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form':form})

def custom_logout(request):
    logout(request)
    return redirect('login')

def bookmark_view(request):
    # Fetch user's bookmarks and pass them to the template
    bookmarks = []  # Fetch user's bookmarks from the database or any other source
    return render(request, 'news_api/bookmarks.html', {'bookmarks': bookmarks})


@login_required
def bookmark_article(request, article_id):
    Bookmark.objects.create(user=request.user, article_id=article_id)
    return redirect('home')  # Redirect back to the homepage after bookmarking

@login_required
def bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    bookmarked_articles = []
    for bookmark in bookmarks:
        article_id = bookmark.article_id
        # Fetch article details using the article_id (or any other identifier)
        # Adjust this part based on how your articles are stored
        article_details_url = f'https://newsapi.org/v2/everything?id={article_id}&apiKey={API_KEY}'
        response = requests.get(article_details_url)
        article_details = response.json()
        bookmarked_articles.append(article_details)
    return render(request, 'news_api/bookmarks.html', {'bookmarked_articles': bookmarked_articles})