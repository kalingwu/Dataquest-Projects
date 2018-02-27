import pandas as pd

data = pd.read_csv("CRDC2013_14.csv",encoding="Latin-1")
all_enrollment=data["TOT_ENR_M"].sum()+data["TOT_ENR_F"].sum()

cols = ["SCH_ENR_HI_M",
       "SCH_ENR_HI_F",
       "SCH_ENR_AM_M",
       "SCH_ENR_AM_F",
       "SCH_ENR_AS_M",
       "SCH_ENR_AS_F",
       "SCH_ENR_HP_M",
       "SCH_ENR_HP_F",
       "SCH_ENR_BL_M",
       "SCH_ENR_BL_F",
       "SCH_ENR_WH_M",
       "SCH_ENR_WH_F",
       "SCH_ENR_TR_M",
       "SCH_ENR_TR_F"
       ]
sum_race_gender={}
percentage={}
for each in cols:
    sum_race_gender[each]=data[each].sum()
    percentage[each]=sum_race_gender[each]/all_enrollment
    print(each +":" + str(percentage[each]))