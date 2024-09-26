from django.shortcuts import render
from django.shortcuts import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name="index.html"