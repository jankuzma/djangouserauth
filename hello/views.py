from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from hello.forms import AddPersonForm, AddProducerForm
from hello.models import Genre, Person, Producer


# Create your views here.
def hello(request):
    return render(request, "hello.html", {"name": "World"})

class AddGenreView(View):
    def get(self, request):
        return render(request, 'genreform.html')
    def post(self, request):
        name = request.POST.get('name')
        g = Genre(name=name)
        g.save()

        return redirect('genrelist')

class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'genrelist.html', {'genres':genres})


class AddPersonView(View):
    def get(self, request):
        form = AddPersonForm()
        return render(request, 'personform.html', {'form':form})
    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(
                **form.cleaned_data
            )
            return redirect('addperson')
        else:
            return HttpResponse('invalid data')

class AddProducerView(View):
    def get(self, request):
        form = AddProducerForm()
        return render(request, 'producerform.html', {'form':form})
    def post(self, request):
        form = AddProducerForm(request.POST)
        if form.is_valid():
            Producer.objects.create(
                **form.cleaned_data
            )
            return redirect('producerform')
        else:
            return HttpResponse('invalid data')

class ProducerListView(View):
    def get(self, request):
        producers = Producer.objects.all()
        return render(request, 'producer_list.html', {"producers":producers})