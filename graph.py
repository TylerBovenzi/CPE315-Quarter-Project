
import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('L1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ' ')
      
    for row in plots:
        x.append(pow(2, int(row[0])))
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g',label = "L1")
x = []
y = []
with open('L2.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')

    for row in plots:
        x.append(pow(2, int(row[0])))
        y.append(int(row[1]))

plt.plot(x, y, color='r', label="L2")

plt.xlabel('Size')
plt.ylabel('CacheMisses')
plt.xscale('log', base=2)
plt.title('Misses')
plt.legend()
plt.show()
