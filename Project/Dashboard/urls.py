from os import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.akus_dashboard, name='akus_dashboard'),
    path('graph_view', views.graph_view, name='graph_view'),
    path('grafana_data', views.grafana_data, name='grafana_data'),
    path('plotly_graph', views.plotly_graph, name='plotly_graph'),
    path('graph_type', views.graph_type, name='graph_type'),
    path('icmp', views.icmp, name='icmp'),
    path('home_network',views.home_network,name='home_network'),
    path('cctv', views.cctv, name='cctv'),
   
]
