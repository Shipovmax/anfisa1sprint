from typing import TypedDict

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render


class IceCream(TypedDict):
    id: int
    title: str
    description: str


ice_cream_catalog: list[IceCream] = [
    {
        'id': 0,
        'title': 'Classic sundae',
        'description': 'Real ice cream for true flavor enthusiasts. '
                       'If a sundae appears on the table, it will not last long.',
    },
    {
        'id': 1,
        'title': 'Ice cream with grasshoppers',
        'description': 'Colombian-style ice cream '
                       'with real caramelized grasshoppers.',
    },
    {
        'id': 2,
        'title': 'Cheddar-flavored ice cream',
        'description': 'The taste of real cheese in a waffle cone.',
    },
]


def ice_cream_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Render a single catalog entry by index.

    Raises:
        Http404: if `pk` is out of range of the hardcoded catalog list
            (previously an unhandled IndexError leaked as a 500 error).
    """
    template = 'ice_cream/detail.html'
    try:
        ice_cream = ice_cream_catalog[pk]
    except IndexError:
        raise Http404(f'Ice cream with id={pk} does not exist')
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request: HttpRequest) -> HttpResponse:
    """Render the full ice cream catalog."""
    template = 'ice_cream/list.html'
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, template, context)
