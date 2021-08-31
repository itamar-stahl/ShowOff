from os import name
from .fake_data_generator import FAKE_GROUP_NAME
from django.shortcuts import render
from django.http import HttpResponse
from .stats_processor import *
from .fake_data_generator import make_fake_db
from django.db.models import Avg
from django.db.models import Sum

WINNER_MSG = "Well Done!"
LOOSER_MSG = "You can get better :)"

TXT_VIEWER = "stats_presentor/textOnly.html"
CHART_VIEWER = "stats_presentor/simpleBarChart.html"
OPEN_MSG_1 = "Snow White asked the seven dwarfs to use ShowOff."
OPEN_MSG_2 = "Usage statistics for "



def index(request):
    return HttpResponse("test")

def fake_new(request):
    return fake(request,TimeRange.YESTERDAY, True)
    
def fake(request, period=TimeRange.YESTERDAY, always_make_new_=False):
    make_fake_db(always_make_new=always_make_new_)
    fake_group = Group.objects.get(name=FAKE_GROUP_NAME)
    vars_dic = extract_view_vars(fake_group, period, None)
    
    return render(request, CHART_VIEWER, vars_dic)

def extract_view_vars(group, period, custom_period=None, estimator=Avg):
    if period == TimeRange.YESTERDAY:
        estimator = Sum
    if estimator == Avg:
        x_axis_label = "Screen hours (average)"
    else:
        x_axis_label = "Screen hours"
    if custom_period is not None:
        pass # TODO
    stats = genarate_stats(group, period, custom_period, estimator)
    
    return {
        "open_msg_1": OPEN_MSG_1,
        "title": OPEN_MSG_2 + period.value.lower() +":",
        "stats_table": stats,
        "x_axis_label": x_axis_label,
        "winner": stats[0][0],
        "losser": stats[len(stats)-1][0],
        "winner_msg": WINNER_MSG,
        "losser_msg": LOOSER_MSG,
    }
    