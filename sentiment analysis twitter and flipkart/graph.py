import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv("train.csv",encoding = "ISO-8859-1")
df1=df1["Sentiment"]
#print(df1)
df2=pd.read_csv("submissioncomp.csv",encoding = "ISO-8859-1")
df2=df2[:99989]
df2=df2["polarity"]
#print(df2)
plt.figure()

df1.plot.bar()
