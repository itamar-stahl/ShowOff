from ShowOff_srv.utils import Estimetor, TimeRange, extract_period

from data_manager.models import Record, MissingRecords
from user_manager.models import User, Group



def process_incomplete_records(group, time_range, custom_period, estimator):
    pass # TODO

def genarate_stats(group, time_range, custom_period, estimator):
    group_members = group.members.all()
    group_stats = []
    first_day, last_day = extract_period(time_range, custom_period)
    try:
        for user in group_members:
            overall_time, distracting = Record.get_user_usage(user, first_day, last_day, estimator)
            group_stats.append([str(user.name), overall_time, distracting])
        group_stats.sort(key=lambda user_stats: user_stats[1])
        return group_stats   
    except MissingRecords:
        return process_incomplete_records(group, time_range, custom_period, estimator)
        
        
    
