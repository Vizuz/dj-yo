from django.shortcuts import render
from .models import Article, Comment


def index(requst) : 
    latest_articles_list=Article.objects.order_by("-pub_date")[:5]
    return render(requst, "articles/list.html", {latest_articles_list:"latest_articles_list"})