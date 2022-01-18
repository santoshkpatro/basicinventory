from django.shortcuts import render


def overview(request):
    return render(request, 'dashboard/overview.html', {'url_name': 'overview'})
