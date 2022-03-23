import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('homework.csv')
rating=df['Avg Rating'].tolist()
graph=ff.create_distplot([rating],['rating'],show_hist=False)
graph.show()