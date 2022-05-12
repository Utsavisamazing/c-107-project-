import pandas as pd 
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")

input = df ["student_id"].to_list()
output = df["level"].to_list()
week= df["attempt"].tolist()

figure = px.scatter(x=input , y=output, color=week )
figure.show()

data1=np.corrcoef(input,output)
print(data1[0][1]) 



