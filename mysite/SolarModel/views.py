from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'SolarModel/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'SolarModel/index.html'
    context_object_name = 'item_list'


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'SolarModel/detail.html', context)

class PlanetDetail(DetailView):
    model = Item
    template_name = 'SolarModel/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('SolarModel:index')

    return render(request, 'SolarModel/item-form.html', {'form': form})

class CreateItem(CreateView):
    model = Item
    fields =['item_name', 'item_size', 'item_mass', 'item_age', 'item_characteristics', 'item_distance']
    template_name = 'SolarModel/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)