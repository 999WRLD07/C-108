import csv
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("phone.csv")
print(df)
df = df["Avg Rating"]
fig = ff.create_distplot([df], ["Ratings"])
print("creating plot")

fig.show()