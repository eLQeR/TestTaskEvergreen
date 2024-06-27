from django.shortcuts import render
from django.views import generic
from test_task.models import Page
from django.template import loader


class IndexView(generic.TemplateView):
    template_name = "index.html"


class PageDetailView(generic.DetailView):
    queryset = Page.objects.all()
    template_name = "page.html"
    context_object_name = "page"
