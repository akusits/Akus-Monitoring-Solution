from plotly.offline import download_plotlyjs, plot
from datetime import datetime
from pybix import GraphImageAPI
import time
from .models import *
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from zabbix.api import ZabbixAPI
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def userlogin(request):
    if request.session.has_key('uid'):
        return redirect('/akus_dashboard')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = User()
        count = User.objects.filter(email=email, password=password).count()
        if count > 0:
            request.session['uid'] = request.POST['email']
            return redirect('/akus_dashboard')
        else:
            messages.error(request, 'Invalid Email And Password')
            return redirect('/')

    return render(request, 'login.html')


def usersignup(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exists ..")
            return redirect('/sign-up')
        else:
            user = User(name=name, cpassword=cpassword, email=email, phone=phone,password=password)
            user.save()
            messages.success(request, "Your Acoount Registered with Us")
            return redirect('/')
    return render(request, 'signup.html')


def deletesession(request):
    del request.session['uid']
    return redirect('/')


def akus_dashboard(request):
    # Moving forward code
    x_data = [0, 10, 21, 38, ]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return render(request, "akus1.html", context={'plot_div': plot_div})

def graph_view(request):

    from pyzabbix.api import ZabbixAPI

    zapi = ZabbixAPI(url='http://172.16.0.32/zabbix',user='Admin', password='zabbix')

    print("Moving Forward...")
    # Create ZabbixAPI class instance

    # Get all monitored hosts
    result1 = zapi.host.get(monitored_hosts=1, output='extend')

    print("Connected to Zabbix API Version %s" % zapi.api_version())




    graph = GraphImageAPI(url="http://172.16.0.32/zabbix",
                      user="Admin",
                      password="zabbix")
    

    # s = zapi.info.version()
    # print (s)
    hosts = zapi.host.get(
        output=["hostid", "name", "description", "lastaccess"])
    hostgroups = zapi.hostgroup.get(
        {"output": "extend", "sortfield": "name"})  # for groupid

    print(hosts)
    print(hostgroups)

    data = []
    s1 = json.dumps(hosts)
    data = json.loads(s1)

    graph = GraphImageAPI(url="http://172.16.0.32/zabbix",
                      user="Admin",
                      password="zabbix")

    graph.get_by_item_names

    # Iterate through the dictionary
    # to print the data.

    for i in hosts:
    
        r = zapi.trigger.get(filter={"host": i}, output=[
                            "triggerid", "description", "priority"])
        print(len(r))

        print(r)
   
        trigger_data = []
        r1 = json.dumps(r)
        trigger_data = json.loads(r1)

    context = {'d': data, 'r': trigger_data}
    # Iterate through the dictionary
    # to print the data.

    list_item = zapi.item.get(filter={"host": 'Grafanatest'})
    #print (len(list_item))
    return render(request, 'zabbix.html', context)


@xframe_options_exempt
def cctv(request):    
    
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'cctv.html', {"results":results})

    

    return render(request, 'cctv.html')


@xframe_options_exempt
def grafana_data(request):
    from grafana_api.grafana_face import GrafanaFace
    from grafanacli import GrafanaAdmin
   
    ga = GrafanaAdmin('http://172.16.0.34:3000')


    # Disable SSL verification
    ga.verify = False
    """SSL verification must be disabled before use GrafanaAuth"""

    # Authentication using username and password
    ga.GrafanaAuth(Username='admin', Password='admin')

    # List your current organization
    x = ga.CurrentOrganization()
    print(x)

    # List all organizations
    u = ga.OrganizationList()
    print(u)
    

    # Search dashboard by title
    dash = ga.DashboardSearch(DashboardName='test')
    #print(dash)
    


    print("------" , '\n', request.headers)

    print("------", '\n', request)
    

    return render(request, 'grafana_check.html')

@xframe_options_exempt
def home_network(request):
    from grafana_api.grafana_face import GrafanaFace
    from grafanacli import GrafanaAdmin
   
    ga = GrafanaAdmin('http://172.16.0.34:3000')


    # Disable SSL verification
    ga.verify = False
    """SSL verification must be disabled before use GrafanaAuth"""

    # Authentication using username and password
    ga.GrafanaAuth(Username='admin', Password='admin')

    # List your current organization
    x = ga.CurrentOrganization()
    print(x)

    # List all organizations
    u = ga.OrganizationList()
    print(u)
    

    # Search dashboard by title
    dash = ga.DashboardSearch(DashboardName='test')
    #print(dash)
    


    print("------" , '\n', request.headers)

    print("------", '\n', request)
    

    return render(request, 'home_network.html')

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
import plotly

import plotly.offline as opy
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

def graph_function():
    

    labels = [1, 2, 3, 4]
    values = [10, 20, 30, 40]
    ndata = 100
    dfi = pd.DataFrame({'date': {0: '2020.01.01',
                                 1: '2020.01.01',
                                 2: '2020.01.01',
                                 3: '2020.01.01',
                                 4: '2020.01.01',
                                 5: '2020.01.01',
                                 6: '2020.02.01',
                                 7: '2020.02.01',
                                 8: '2020.02.01',
                                 9: '2020.02.01',
                                 10: '2020.02.01',
                                 11: '2020.02.01',
                                 12: '2020.03.01',
                                 13: '2020.03.01',
                                 14: '2020.03.01',
                                 15: '2020.03.01',
                                 16: '2020.03.01',
                                 17: '2020.03.01'},
                        'sub_id': {0: 1233,
                                   1: 1233,
                                   2: 1233,
                                   3: 3424,
                                   4: 3424,
                                   5: 3424,
                                   6: 1233,
                                   7: 1233,
                                   8: 1233,
                                   9: 3424,
                                   10: 3424,
                                   11: 3424,
                                   12: 1233,
                                   13: 1233,
                                   14: 1233,
                                   15: 3424,
                                   16: 3424,
                                   17: 3424},
                        'stat_type': {0: 'link_clicks',
                                      1: 'alerts',
                                      2: 'triggers',
                                      3: 'link_clicks',
                                      4: 'alerts',
                                      5: 'triggers',
                                      6: 'link_clicks',
                                      7: 'alerts',
                                      8: 'triggers',
                                      9: 'link_clicks',
                                      10: 'alerts',
                                      11: 'triggers',
                                      12: 'link_clicks',
                                      13: 'alerts',
                                      14: 'triggers',
                                      15: 'link_clicks',
                                      16: 'alerts',
                                      17: 'triggers'},
                        'value': {0: 12,
                                  1: 50,
                                  2: 9,
                                  3: 24,
                                  4: 100,
                                  5: 18,
                                  6: 14,
                                  7: 24,
                                  8: 39,
                                  9: 20,
                                  10: 10,
                                  11: 8,
                                  12: 4,
                                  13: 2,
                                  14: 3,
                                  15: 2,
                                  16: 1,
                                  17: 1}})


    # change some types
    dfi['date'] = pd.to_datetime(dfi['date'])
    dfi['sub_id'] = dfi['sub_id'].astype(str)
    df = dfi

    # split df by stat_type and organize them in a dict
    groups = df['stat_type'].unique().tolist()
    dfs = {}
    for g in groups:
        dfs[str(g)] = df[df['stat_type'] == g]

    # pivot data to get different sub_id across dates
    dfp = {}
    for df in dfs:
        dfp[df] = dfs[df].pivot(index='date', columns='sub_id', values='value')

    # one trace for each column per dataframe
    fig = go.Figure()

    # set up the first trace
    fig.add_trace(go.Scatter(x=dfp['link_clicks'].index,
                            y=dfp['link_clicks']['1233'],
                            visible=True)
                )

    fig.add_trace(go.Scatter(x=dfp['link_clicks'].index,
                            y=dfp['link_clicks']['3424'],
                            visible=True)
                )

    # plotly start
    # buttons for menu 1, names
    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for df in dfp.keys():
        buttons.append(dict(method='restyle',
                            label=df,
                            visible=True,
                            args=[{'y': [dfp[str(df)]['1233'].values, dfp[str(df)]['3424'].values],
                                'x':[dfp[str(df)].index],
                                'type':'scatter'}],
                            )
                    )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)
    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True

    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu)

    # add notations to the dropdown menus
    fig.update_layout(
        annotations=[
            go.layout.Annotation(text="<b>stat_type:</b>",
                                x=-0.3, xref="paper",
                                y=1.1, yref="paper",
                                align="left", showarrow=False),
        ]
    )

    plt_div = plotly.offline.plot(fig, output_type='div')

    return plt_div


def plotly_graph(request):
    my_graph = graph_function()
    context = {'graph': my_graph}
    return render(request, 'graph.html', context)


def typegraph():
    import plotly.express as px



    df = pd.read_csv(
        'https://raw.githubusercontent.com/Aakritisingla1895/akus_monitoring_csv/master/Panel%20Title-data-2021-02-15%2018%2025%2059.csv')

    fig1 = px.scatter(df,
                x='Time',
                y='A-series',
            )
    plt2_div = plotly.offline.plot(fig1, output_type='div')

    return plt2_div


def type2graph():
    import plotly.express as px
    

    df = pd.read_csv(
        'https://raw.githubusercontent.com/Aakritisingla1895/akus_monitoring_csv/master/Panel%20Title-data-2021-02-15%2018%2025%2059.csv')

    fig2 = px.line(df,
                      x='Time',
                      y='A-series',
                    )
    plt2_div2 = plotly.offline.plot(fig2, output_type='div')

    return plt2_div2

    


def graph_type(request):
    type_graph = typegraph()
    type_graph2 = type2graph()
    context = {'graph': type_graph, 'graph2':type_graph2}
    return render(request, 'new_graph.html', context)


def icmp(request):
    import os
    import requests

    import time

    url="http://www.medium.com"


    with open('/home/akus/Documents/Project/Dashboard/ping.txt') as file:

        sw = file.read()
        sw = sw.splitlines()

    for ip in sw:

        website_response=requests.get(ip)
        response= website_response.status_code
        if response == 200:
            print (f"Status is OK, and {ip} is UP") 
        elif response == 404:
            print (f"Status is BAD, and {ip} is DOWN") 
        else:

            print (f"Status is BAD, and {ip} is DOWN") 

    return render(request, 'icmp.html')

