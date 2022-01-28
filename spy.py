import matplotlib.pyplot as plt
import numpy as np
import csv

from numpy.lib.shape_base import split

import time_tool

invest = 10000
keep = 0


price = []
day = []
date = []
def load_bitcoin():
    path = 'SPY.csv'
    with open(path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(rows):
            # if(i>50):
            #     break
            if(i == 0):
                continue
            if(row[1] == "null"):
                continue
            price.append(float(row[1]))
            day.append(i)
            date.append(row[0])

def show_chart():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(day, price)
    plt.show()

load_bitcoin()
#show_chart()

#print(date)
'''
ALT = 0
count = 0
for i in range(1000, len(price)):
    if(price[i] > ALT):
        ALT = price[i]

    if(price[i] < ALT*0.9):
        print(date[i], price[i])
        ALT = price[i]
        count = count+1
print("count = ", count)
'''
stock, share = [], []
for i in range(0, len(price)):
    d = date[i].split("-")
    if((d[0]=="2009" and d[1] > "05") or d[0] > "2009"):
        next_month = time_tool.month_change(date[i], before=date[i-1]) if i> 0 else time_tool.month_change(date[i])
        #print(next_month, "next_month")
        if(next_month == False):
            stock.append(price[i])
            share.append(300/price[i])
            #print(date[i])

total = 0
for i in range(0, len(stock)):
    total = total + stock[i]*share[i]
print("average cost = ",total/sum(share), "Margin = ",price[-1]/(total/sum(share)))

print(sum(stock)/len(stock))
print(price[-1], "fianl price")
#print(price[-1]/(sum(stock)/len(stock)))
print(len(stock))
print(sum(share)*price[-1], "total money")
print(sum(share)*price[-1]/(300*len(stock))*100, "%")