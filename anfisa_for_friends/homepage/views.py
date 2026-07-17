from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Render the landing page."""
    template = 'homepage/index.html'
    return render(request, template)
