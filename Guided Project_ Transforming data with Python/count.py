import read
from collections import Counter
df = read.load_data()
headline = df["headline"]
string = ""

for each in headline:
    string+=str(each) + " "
    
string = string.lower()
string_split = string.split()
print(Counter(string_split).most_common(100))