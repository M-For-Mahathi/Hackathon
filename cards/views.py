from django . urls import reverse_lazy
from django . views . generic import (
    ListView,
    CreateView,
    UpdateView,
)
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from .models import Card
import random
from django.shortcuts import render

def index(request):
    return render(request, 'build/index.html')

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all()

class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

class BoxView(CardListView):
    template_name = "cards/box.html"

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
        
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer