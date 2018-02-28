import pandas as pd

def load_data():
    data = pd.read_csv("hn_stories.csv")
    print("read")
    data.columns = ["submission_time","upvotes","url","headline"]
    return data
