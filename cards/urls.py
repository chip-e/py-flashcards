# cards/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.CardListView.as_view(), name="card-list"),
    path("new",views.CardCreateView.as_view(), name="card-create"),# route connecting to CardCreateView
    path("edit/<int:pk>",views.CardUpdateView.as_view(),name="card-update"),
# pk: primary key, database entry's unique identifier, added automatically by django at entry creation
# <int:pk> points to CardUpdateView, the <int:pk> part of the URL allows primary key as an int
#       CardUpdateView will return data for the corresponding card
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"),

]

