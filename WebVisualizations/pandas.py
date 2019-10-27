import pandas as pd

df = pd.read_csv("cities.csv")

table = pd.to_html(df)

table.replace('\n','')

df.to_html('data.html')
