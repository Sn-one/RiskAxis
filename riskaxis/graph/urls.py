from django.urls import path

from .views import erm_graph

app_name = "graph"

urlpatterns = [
    path("erm/", erm_graph, name="erm"),
]
