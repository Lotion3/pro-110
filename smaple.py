import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
readGPA=df["average"].tolist()

dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(readGPA))
    value=readGPA[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
mean2=statistics.mean(readGPA)
print("Whole data mean"+str(mean))
print("Sample data mean"+str(mean2))
stDev=statistics.stdev(dataset)
mode=statistics.mode(dataset)
median=statistics.median(dataset)

fig=ff.create_distplot([dataset],["Random 100"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
fig.show()