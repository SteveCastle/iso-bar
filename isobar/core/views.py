from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
import random
from core.models import Article

class HomeView(TemplateView):
    template_name = "home.html"


class Articles(ListView):
    template_name = "articles.html"
    model = Article


class ArticleDetail(DetailView):
    template_name = "article.html"
    model = Article


def cool_view(request):

	last_names = ["Castle", "Smith", "Rogers"]
	x = "Steve " + last_names[random.randint(0,2)]
	return HttpResponse('HELLO! ' + str(x))