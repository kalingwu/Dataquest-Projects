import read
import pandas as pd
import dateutil as dt

df = read.load_data()

def date_time(timestamp):
    date_time_obj = dt.parser.parse(timestamp)
    return date_time_obj.hour
    
df["hour"] = df["submission_time"].apply(date_time)
print(df["hour"].value_counts())