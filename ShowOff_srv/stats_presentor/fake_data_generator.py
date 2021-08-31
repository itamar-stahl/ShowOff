from os import name
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from data_manager.models import *
from ShowOff_srv.utils import *
from ShowOff_srv.settings import *



SIGMA = 1.9
FAKE_PASSWORD ='LD3pClbD9cL8Z4PlnYtt'
FAKE_KEY ='Jhsj#y1F@ZjKt#0m,HL8YUxjOdcRTvUfvzTe6t!dMW`/9Z6*$'
FAKE_GROUP_NAME = 'FAKE-Kt#0m,HL8YUxhsj#yjOdcRTvUfvzTe6'
FAKE_STAT_PAGE_MSG = "Snow White asked the seven dwarfs to install the ShowOff app on their mobiles. Here are the results:\n" 
FAKE_USERS = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]

pd.set_option('display.max_rows', 300)

def draw_hist(s, mu, sigma):
    print("mu: ", mu)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
    plt.show()

def get_fake_table_df(seed = None, sigma=SIGMA):
    if seed is not None:
        np.random.seed(seed)
    yesterday = get_yesterday()
    dates_list = [(yesterday - dt.timedelta(days=j)).strftime("%Y-%m-%d") for j in range(MAX_DAYS)]
    means = np.random.uniform(2, 5.5, size=(MAX_USERS,))

    fake_overall_time = np.array([])
    for i in range(MAX_USERS):
        new =  np.random.normal(means[i], sigma, size=MAX_DAYS) 
        new += 0.33* np.random.uniform(0, means[i], size=MAX_DAYS)
        new = np.minimum(15.0, np.maximum(0.0,new))
        new = new.round(2)
        #draw_hist(new, means[i], sigma)
        fake_overall_time = np.append(fake_overall_time, new)
        

    fake_distracting_time_fraction = np.random.uniform(0.5, 0.7, size=(MAX_DAYS*MAX_USERS)) + 0.2*(fake_overall_time/10)
    fake_distracting_time = (fake_distracting_time_fraction * fake_overall_time).round(2)
    
    index = pd.MultiIndex.from_product([list(range(1,8)), dates_list], names = ["user_id", "date"])
    df = pd.DataFrame(index = index).reset_index().set_index("date").reset_index()
    df.index.names = ['id']
    df["overall_time"] = pd.DataFrame(data= fake_overall_time)
    df["distracting_time"] = pd.DataFrame(data= fake_distracting_time)
    df["original_data"] = True
    user = df.pop('user_id')
    df["user_id"] = user
    
    return df
    
    
def create_fake_users(fake_group):
    for user_name in FAKE_USERS:
        user = User(name=user_name, email=f"{user_name}@fake.com", password=FAKE_PASSWORD, group=fake_group)
        user.save()

def make_fake_db(seed = None, sigma=SIGMA, always_make_new=False):
    
    yesterday = get_yesterday()
    month_ago = get_month_ago()
    try:
        fake_group = Group.objects.get(name=FAKE_GROUP_NAME)
    except Group.DoesNotExist:
        fake_group = Group(name=FAKE_GROUP_NAME, key=FAKE_KEY)
        fake_group.save()
        create_fake_users(fake_group)   
    num_of_records = Record.get_group_usage(fake_group, *extract_period(TimeRange.LAST_MONTH)).count()
    if always_make_new or num_of_records != MAX_DAYS*MAX_USERS:
        Record.objects.filter(user__group=fake_group).delete() 
        table = get_fake_table_df()
        df_to_db(table, "data_manager_record")
       
           
 
    


    