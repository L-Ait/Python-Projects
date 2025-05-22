'''
This project uses a random uniform distribution of points to integrate 
a definite integral of a given function.
'''

# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt

# Define function to be integrated 
def func(x):
    return (-1 * np.sin(x))/x

# Set number of points and limits of integration
N = 2000
a, b = np.pi, 4*np.pi
# Set limits of the region to spread the points
yMin, yMax = -0.15, 0.25

# Create Monte Carlo sample in the rectangular region from the limits above
x = np.random.uniform(a, b, N)
y = np.random.uniform(yMin, yMax, N)

# Plot graph and x axis line
plt.figure(figsize=(16,9))
xPlot = np.linspace(a, b, 101)
xAxis = np.linspace(0, 0, 101)
yPlot = func(xPlot)
plt.plot(xPlot, yPlot, 'black')
plt.plot(xPlot, xAxis, 'black')

# Plot MC points with different colours depending on their location
total = 0
RGBPos = 0
RGBNeg = 0
for i in range(N):
    if y[i] <= func(x[i]) and y[i] >= 0:
        total += 1
        RGBPos += 1
        plt.plot(x[i], y[i], '.', color = 'blue')
    elif y[i] >= func(x[i]) and y[i] < 0:
        total -= 1
        RGBNeg += 1
        plt.plot(x[i], y[i], '.', color = 'red')
    else:
        plt.plot(x[i], y[i], '.', color = 'black')

# Calculate integral estimate
area = (total/N) * (0.4 * 3 * np.pi)

plt.title(r"Approximate Integral of $-sin(x)/x$ using a Monte Carlo Method")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.grid()
plt.show()

print("The integral of the function, according to the Monte Carlo method, is", area, "\n")

# Create a graphic of the average colour of the points
plt.figure(figsize=(3,3))
col_avg = (RGBPos*np.array([0,0,1])+RGBNeg*np.array([1,0,0]))/N
plt.plot(0, 0, 's', markersize = '500', color = (col_avg[0], col_avg[1], col_avg[2]))
plt.title("Average Colour of All Points")
plt.axis('off')
plt.show()