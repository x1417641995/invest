import matplotlib.pyplot as plt
import numpy as np
import csv

from numpy.lib.shape_base import split

invest = 10000
keep = 0


price = []
day = []
def load_bitcoin():
    path = 'BTC-USD.csv'
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

def show_chart():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(day, price)
    plt.show()

load_bitcoin()
#show_chart()
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(day, price)
#plt.show()

invest = 10000
keep = 0
current, goal = 10000, price[0]*10
rate = 1
save = 0
split_price = price[0]
goal_rate = 10
for i in price:
    #pass
    if(i > goal):
        current = current*rate*(i/split_price)
        save = save + current*(1-rate)
        goal = goal*goal_rate

        split_price = i
    
    if(i < split_price//2):
        current = current*(i/split_price) +  save/2
        save = save/2
        goal = split_price//2 * goal_rate
        split_price = i

current = current * (price[-1]/split_price)

print(save, "save")
print(current, "current")
print(save + current, "sum")