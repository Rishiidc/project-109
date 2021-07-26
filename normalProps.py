import pandas as pd 
import statistics as stats 
import plotly.figure_factory as pff 

data = pd.read_csv("StudentsPerformance.csv")
mathsc = data["mathscore"].tolist()

mean = stats.mean(mathsc)
median = stats.median(mathsc)
mode = stats.mode(mathsc)
standardDeviation = stats.stdev(mathsc)

fsdstart,fsdend = mean - standardDeviation, mean + standardDeviation
data1 = [result for result in mathsc if fsdstart<result<fsdend]

ssdstart,ssdend = mean - 2*standardDeviation, mean + 2*standardDeviation
data2 = [result2 for result2 in mathsc if ssdstart<result2<ssdend]

tsdstart,tsdend = mean - 3*standardDeviation, mean + 3*standardDeviation
data3 = [result3 for result3 in mathsc if tsdstart<result3<tsdend]

print(fsdstart,fsdend)
print(mean,mode,median,standardDeviation)
print(len(data1)/len(mathsc))
print(len(data2)/len(mathsc))
print(len(data3)/len(mathsc))
print("{} -> Percentage data in data1".format(len(data1)/len(mathsc)))
print("{} -> Percentage data in data2".format(len(data2)/len(mathsc)))
print("{} -> Percentage data in data3".format(len(data3)/len(mathsc)))