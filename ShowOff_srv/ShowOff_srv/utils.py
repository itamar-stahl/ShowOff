from ShowOff_srv.settings import DATABASES
import datetime as dt
import sqlite3
from enum import Enum


# Project's constants and enums

MAX_USERS = 7
MAX_DAYS = 30

class TimeRange(Enum):
    YESTERDAY = "Yesterday"
    LAST_WEEK = "Last 7 days"
    LAST_MONTH = "Last 30 days"
    CUSTUM = "Custom"
    
class Estimetor(Enum):
   SUM = 1
   AVERAGE = 2
   MEDIAN = 3
   MIN = 4
   MAX = 5
    

def get_yesterday():
    return (dt.datetime.today().date() - dt.timedelta(days=1))

def get_week_ago():
    return (dt.datetime.today().date() - dt.timedelta(days=7))

def get_month_ago():
    return (dt.datetime.today().date() - dt.timedelta(days=29))

def extract_period(time_range, custom_period=None):
    last_day = yesterday = get_yesterday()
    if time_range == TimeRange.YESTERDAY:
        first_day = yesterday
    elif time_range == TimeRange.LAST_WEEK:
        first_day = (yesterday - dt.timedelta(days=6))
    elif time_range == TimeRange.LAST_MONTH:
        first_day = (yesterday - dt.timedelta(days=29))
    else:
        first_day, last_day = custom_period[0], custom_period[1] # TODO CHECK VALIDITY
    return first_day, last_day

def df_to_db(df, table_name):
    db = DATABASES['default']['NAME']
    connection = sqlite3.connect(db)
    df.to_sql(table_name, con=connection, if_exists='append')
        
    