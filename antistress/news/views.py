from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm, Testans
from django.views.generic import DetailView, UpdateView, DeleteView


def test_home(request):
    test = Test.objects.order_by('id')
    return render(request, 'news/test_home.html', {'tests': test})


def index1(request):
    test = Test.objects.order_by('id')
    return render(request, 'news/finally.html', {'tests': test})


def index2(request):
    test = Test.objects.order_by('id')
    return render(request, 'news/finally2.html', {'tests': test})


def index3(request):
    test = Test.objects.order_by('id')
    return render(request, 'news/finally3.html', {'tests': test})


class NewsDetailView(DetailView):
    model = Test
    template_name = 'news/details_test.html'
    context_object_name = 'article'


class TestFinili(DetailView):
    model = Test
    template_name = 'news/finally.html'
    context_object_name = 'Fin'


class NewsUpdateView(UpdateView):
    model = Test
    template_name = 'news/create_test.html'
    context_object_name = 'update'

    form_class = TestForm


class NewsDeliteView(DeleteView):
    model = Test
    success_url = '/news/'
    template_name = 'news/test-delete.html'


def create_test(request):
    error = ''
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неккорктна'
    form = TestForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create_test.html', data)


def test_work(request):
    error = ''
    if request.method == "POST":
        form = Testans(request.POST)
        if not (form.is_valid()):
            return redirect('home')
        else:
            error = 'Форма была неккорктна'
    tests = Test.objects.order_by('id')
    form = Testans

    data = {
        'form': form,
        'error': error,
        'tests': tests
    }
    return render(request, 'news/test_work.html', data)

# def create_test(request):
#     return render(request, 'news/create_test.html')
