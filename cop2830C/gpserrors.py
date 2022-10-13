import csv
import matplotlib.pyplot as plt
x=[]
y=[]
with open('/Users/jj/Downloads/gps_day.csv', 'r') as cvsfile:
    lines = csv.reader(cvsfile, delimiter= ',')
    for row in lines:
       x.append(row[0])
       y.append(float(row[1]))

plt.scatter(x, y)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('GPS Errors')
plt.show()