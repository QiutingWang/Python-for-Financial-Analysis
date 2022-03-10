#Index and select data:square bracket--limited functionality,loc and iloc

#extract for one column
brics[['country']] #if you want to select the country column but keep the data in a dataframe-->need a double square brackets
#extract for two column
brics[["country", "capital"]]
#row selection
brics[1:4] #slice is exclusive and that the index start 0,and here exists an index
#loc-->label based;iloc-->integer position-based
#row access loc
brics.loc["RU"]#-->row as pandas series
brics.loc[["RU"]]#-->row as dataframe
brics.loc[["RU", "IN", "CH"]]#-->multiple dataframe
#row and column loc
brics.loc[["RU", "IN", "CH"], ["country", "capital"]]  #the intersection get returned
brics.loc[:, ["country", "capital"]] #the intersection span all rows
#row access iloc
brics.iloc[[1,2,3]] #return the dataframe include the first three rows
brics.iloc[[1,2,3], [0, 1]]
brics.iloc[:, [0,1]]

##iterrows##Iterate over DataFrame rows as (index, Series) pairs.https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():  #change the row label to lab,row data as row
    print(lab) #return a series
    print(row)

import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])
    
#add column-using len()
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows() :
    # - Creating Series on every iteration,add new column
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)

#add column-using apply()
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
brics["name_length"] = brics["country"].apply(len)
print(brics)



##Representing time with Datetime##
from datetime import datetime
black_monday = datetime(1987, 10, 19)
print(black_monday)
datetime.now()

#Datetime from string#
black_monday_str = "Monday, October 19, 1987. 9:30 am"
format_str = "%A, %B %d, %Y. %I:%M %p"
datetime.datetime.strptime(black_monday_str, format_str)
#Year: %y without century; %Y with centry
#Month: %b abbreviated name,%B full name,%m as number
#Day of Month: %d(01,02,...)
#Weekday: %a Abbreviated name(Sun, Mon,...),%w: number
#Hours: %H 24 hour, %I 12 hour,%M 01,02,...59
#Seconds: %S (01,02,03,...59)
#Micro-Sceonds: %f(000000,000001,...999999)
#AM/PM: %p(AM/PM)
#%m month;%M Minutes

"%Y-%m-%d"
"%A, %d %B %y"
dt.strftime(format_string)
great_depression_crash = datetime.datetime(1929, 10, 29)
great_depression_crash
great_depression_crash.strftime("%a, %b %d, %Y")

##Working with datetime##
#comparing date time-->which date comes first,the eariler,the smaller
#EG:Goldman Sachs after TARP?
tarp_first = goldman_sachs > tarp
print(f"It is {tarp_first} that TARP was approved first.")
#the same day:same_time = goldman_sachs == morgan_stanley
#Difference between datetimes:subtraction returns a timedelta object
asian_crisis = datetime(1997, 7, 2)
world_mini_crash = datetime(1997, 10, 27)
delta = world_mini_crash - asian_crisis
type(delta)
delta.days
#Creating relative datetimes#
dt
#datetime.datetime(2019, 1, 14, 0, 0)
datetime(dt.year, dt.month, dt.day - 7)
#datetime.datetime(2019, 1, 7, 0, 0)
datetime(dt.year, dt.month, dt.day - 15)
[ValueError]
<ipython-input-28-804001f45cdb> in <module>()
-> 1 datetime(dt.year, dt.month, dt.day - 15)
ValueError: day is out of range for month

#in order to fit this problem:
delta = world_mini_crash - asian_crisis
type(delta)
#-->datetime.timedelta
from datetime import timedelta
offset = timedelta(weeks = 1)
offset
#datetime.timedelta(7)
dt - offset
#datetime.datetime(2019, 1, 7, 0, 0)
offset = timedelta(days=16)
dt - offset
#datetime.datetime(2018, 12, 29, 0, 0)-->it can return a cross-month result.Timedelta's understanding the boundaries.

cur_week = last_week + timedelta(weeks=1)
# Do some work with date
# set last week variable to cur week and repeat
last_week = cur_week
source_dt = event_dt - timedelta(weeks=4)
# Use source datetime to look up market factors
