from django.shortcuts import render

ice_cream_catalog = [
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


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, template, context)
