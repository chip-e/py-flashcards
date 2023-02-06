# cards/views.py

# Create your views here.
# from django.shortcuts import render
import random

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from .forms import CardCheckForm
from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")

class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create") # reverse_lazy() to refer to card-create route by its name

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

# Creating "BoxView" as subclass of "CardListView"
# Need to overwrite "template_name" to point to box.html template instead of card_list.html
# "box_num" value is passed as keyword argument in GET request
# To use box number in template, use .get_context_data() to add box_num as box_number to view's context 
class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
# randomly picks card, card will be present in learning session in box.html template
# needs self.object_list in case there's no cards in a box
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

# handle incoming POST requests, check forms in back end
# Tries to get Card object from database by card_id if form is valid
# "get_object_or_404" either get card or raise 404 error
# last line redirect request to same page from which the request was posted
# "HTTP_REFERER" stores info about URL that sent the request (box for current session)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))


