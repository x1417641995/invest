import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a, b = 0, 0
rate = 1.2
savey = 30
lista, listb = [], [0,0,0,0,0,0,0]
'''
for i in range(0,42):
    if(i<8):
        a = (a+savey)
    a = a*rate
    lista.append(a)
'''
lista = [0,0,0,0,0,0,0]
for i in range(0,35):
    
    if(i<10):
        a = (a+30)*rate
    elif(i<20):
        a = (a+40)*rate
    else:#if(i<30):
        a = (a+50)*rate
    lista.append(a)

for i in range(0,35):
    b = (b+savey)*rate
    '''
    if(i<10):
        b = (b+30)*rate
    elif(i<20):
        b = (b+40)*rate
    else:#if(i<30):
        b = (b+50)*rate
    '''
    listb.append(b)
d = 0
for i in range(0,35):
    if(i<8):
        d = (d+10)*rate
    d = d*rate

print(a)
print(b)
print(d)

# this def is optimise data readability
# w is 10 thousand, m is million, b is billion
def translate(x):
    if(x>100):
        if(x>100000):
            return str(round(x/100000, 2)) + "b"
        return str(round(x/100, 2)) + "m"
    return str(round(x, 2))


'''
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
'''
# draw line chart
fig, ax = plt.subplots()
ax.plot(list(range(18,60)), lista, label="A", marker='o')
ax.plot(list(range(18,60)), listb, label="B", marker='o')

ax.set(xlabel='years', ylabel='money(w)',
       title='Interest rate '+ str(rate))
ax.grid()

plt.legend(loc = "best", fontsize=20)

# display point
x= list(range(18,60))
for i,j,k in zip(x,listb, lista):
    ax.annotate(translate(j),xy=(i,j-1000))
    #ax.annotate(translate(k),xy=(i,k+1000))

plt.show()


