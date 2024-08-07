from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Home, Divider

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        home = Home.objects.first()
        dividers = Divider.objects.all()

        context = {
            'home':home,
            'dividers':dividers,
        }
        return render(request, self.template_name, context=context)
    
