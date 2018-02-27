import pandas as pd

data = pd.read_csv("CRDC2013_14.csv",encoding="Latin-1")
JJ_counts = data["JJ"].value_counts()
SCH_counts = data["SCH_STATUS_MAGNET"].value_counts()
print(JJ_counts)
print(SCH_counts)

JJ_table = pd.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"],index="JJ",aggfunc="sum")

SCH_table = pd.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"],index="SCH_STATUS_MAGNET",aggfunc="sum")

print(JJ_table)
print(SCH_table)