from logging import warn
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
high, low = [], []

def load_bitcoin():
    path = 'UPRO.csv'
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
            high.append(float(row[2]))
            low.append(float(row[3]))

def show_chart():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(day, price)
    plt.show()

load_bitcoin()
#show_chart()

#print(date)
def find_thritypercent_decreace():
    ALT = 0
    count = 0
    after_month = 99
    for i in range(0, len(price)):
        #if(price[i] > ALT):
        if(high[i] > ALT):
            #ALT = price[i]
            ALT = high[i]

        #if(price[i] < ALT*0.7):
        if(low[i] < ALT*0.7):
            # print(date[i], price[i])
            # ALT = price[i]
            print(date[i], low[i])
            ALT = low[i]

            after_month = i+15
            count = count+1
        
        if(i == after_month):
            print("after_month", date[i], price[i])
    print("count = ", count)

stock = []
def find_thritypercent_decreace2(stock):
    ALT = 0
    count = 0
    after_month = 99
    warnning = False
    earn = 0
    for i in range(0, len(price)):
        #if(price[i] > ALT):
        if(high[i] > ALT):
            #ALT = price[i]
            ALT = high[i]

        if(price[i] < ALT*0.7):
        #if(low[i] < ALT*0.7):
            # print(date[i], price[i])
            ALT = price[i]
            #print(date[i], low[i])
            #ALT = low[i]

            after_month = i+15
            count = count+1
            warnning = True
            #print(stock, "stock")
            earn = earn +( (price[i] - sum(stock)/len(stock))*len(stock) )
            stock = [0]*len(stock)
        
        next_month = time_tool.month_change(date[i], before=date[i-1]) if i> 0 else time_tool.month_change(date[i])
        if(next_month == False and warnning == False ):
            # if(warnning == False):
            #     stock.append(price[i])
            # if(warnning == True):
            #     pass
            stock.append(price[i])


        if(i == after_month):
            print("after_month", date[i], price[i])
            warnning = False
            #stock = [price[i]]*len(stock)
            stock = [price[i]]*int(earn//price[i])
    print("count = ", count)
    earn = earn +( (price[i] - sum(stock)/len(stock))*len(stock) )
    print(earn, len(stock))

def find_thritypercent_decreace3(stock):
    ALT = 0
    count = 0
    after_month = 99
    warnning = False
    earn = 0
    for i in range(0, len(price)):
        if(price[i] > ALT):
            ALT = price[i]

        if(price[i] < ALT*0.7):
            #print(date[i], price[i])
            ALT = price[i]
         
            after_month = i+15
            count = count+1
            warnning = True
            #print(stock, "stock")
            earn = earn +( (price[i] - sum(stock)/len(stock))*len(stock) )
            stock = [0]*len(stock)
        
        next_month = time_tool.month_change(date[i], before=date[i-1]) if i> 0 else time_tool.month_change(date[i])
        if(next_month == False and warnning == False ):
            # if(warnning == False):
            #     stock.append(price[i])
            # if(warnning == True):
            #     pass
            stock.append(price[i])


        if(i == after_month):
            print("after_month", date[i], price[i])
            warnning = False
            #stock = [price[i]]*len(stock)
            stock = [price[i]]*int(earn//price[i])
    print("count = ", count)
    earn = earn +( (price[i] - sum(stock)/len(stock))*len(stock) )
    print(earn, len(stock))
    print("ALT*0.7", ALT*0.7)
find_thritypercent_decreace2(stock)
stock = []
find_thritypercent_decreace3(stock)

stock = []
for i in range(0, len(price)):
    next_month = time_tool.month_change(date[i], before=date[i-1]) if i> 0 else time_tool.month_change(date[i])
    #print(next_month, "next_month")
    if(next_month == False):
        stock.append(price[i])
        #print(date[i])

print(sum(stock)/len(stock))
print(price[-1], "fianl price")
print(price[-1]/(sum(stock)/len(stock)))
print(len(stock))
print(price[-1]/price[1], "raise", price[-1], price[1])
print((price[-1] - sum(stock)/len(stock))*len(stock), len(stock) )