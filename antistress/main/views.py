from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'value': ['side', 'hello', 'array'],
    }
    return render(request, 'main/index.html', data)


def adobe(request):
    return render(request, 'main/adobe.html')
