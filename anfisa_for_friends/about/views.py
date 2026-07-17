from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def description(request: HttpRequest) -> HttpResponse:
    """Render the static "about" page."""
    template = 'about/description.html'
    return render(request, template)
