'''
End of file for docs
This module helps formatting fetched data into pandas dataframe and json formats.
Dependencies : pandas, json
'''
import pandas as pd
from datetime import datetime
from datetime import date
today = date.today()
date_object=today.strftime("%b-%d-%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
def makedf(s):
    print(s)
    l = s.split("\n")
    name = l[2]
    vehName = l[6]
    regNo = l[10]
    regDate = date_object
    Time=current_time
    data = [['Name',name], ['Vehicle Name',vehName], ['Registration Number',regNo],['Date',regDate],['Time',Time]]
    df = pd.DataFrame(data)
    return df

