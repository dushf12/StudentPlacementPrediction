import pandas as pd
df = pd.read_csv("testdata.csv")
print(df.get("TechnicalSkills")[0])