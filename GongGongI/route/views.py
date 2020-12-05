from django.shortcuts import render


def index(request):
    return render(
        request,
        'map/index.html',
        {
            'wjh_test': 'wjh_test20201204',
        }
    )


def map(request):
    return render(
        request,
        'map/map.html',
        {
            'wjh_test': 'wjh_test20201204',
        }
    )
