# This small project computes a Taylor series (power series) approximation of the sine(x) and log(1+x) functions and 
# plots the results of the approximation for various values of N against the true values. The error plot for the 
# sine function is also computed and plotted.

# Import standard libraries
import numpy as np
import matplotlib.pyplot as plt

#################
# Sine Function #
#################

# Define the Taylor (power) series approximation for sine and range of values 
N = 0
x = np.arange(-3*np.pi, 3*np.pi, 0.1)

def taylorSinApprox(x, N):
    sinSum = np.zeros(len(x))
    for n in range(0, N+1):
        sinSum = sinSum + ((-1)**n)*(x**(2*n+1))/np.math.factorial(2*n+1)
    return sinSum
  
# Define true value of sin(x) from the NumPy library
sinFunc = np.sin(x)

# Plot each sin(x) approximation corresponding to the chosen value of N
plt.figure(figsize=(25,10))
for N in range(0,7):
    plt.plot(x, taylorSinApprox(x, N), '--')

# Plot the true value for sin(x)
plt.plot(x, sinFunc)

# Set up the matplotlib environment
plt.title(r"$\sin(x)$ Graph and its Taylor Expansion Approximation for Various Values of N", fontsize=12)
plt.xlim(-3*np.pi, 3*np.pi)
plt.xlabel(r'$x$',fontsize='16')
plt.ylim(-5,5)
plt.ylabel(r'$\sin(x)$',fontsize='16')
plt.grid(True)
plt.show()

#################
# Log Function #
#################

# Define the function to approximate log(1+x) using the Taylor series expansion
N = 0
x = np.arange(-0.9, 2, 0.05)

def taylorLogApprox(x, N):
    logSum = np.zeros(len(x))
    for n in range(1, N+1):
        logSum = logSum + ((-1)**(n+1))*(x**n)/n
    return logSum

# Define true value of sin(x) from the NumPy library
logFunc = np.log(1+x)

# Plot each log(1+x) approximation corresponding to the chosen value of N
plt.figure(figsize=(25,10))
for N in range(1,8):
    plt.plot(x, taylorLogApprox(x, N), '--')

# Plot the true value for log(1+x)
plt.plot(x, logFunc)

# Set up the matplotlib environment
plt.title(r"$\log(1+x)$ Graph and its Taylor Expansion Approximation for Various Values of N", fontsize=12)
plt.xlim(-1, 2)
plt.xlabel(r'$x$',fontsize='16')
plt.ylim(-3,4)
plt.ylabel(r'$\log(1+x)$',fontsize='16')
plt.grid(True)
plt.show()

###############
# Error Plots #
###############

# Define a new function that corresponds to the error in the approximation
N = 0
x = np.arange(-3*np.pi, 3*np.pi, 0.1)

def taylorError(x, N):
    diff = np.zeros(len(x))
    for n in range(0, N+1):
        diff = abs(taylorSinApprox(x, N)-np.sin(x))
    return diff

# Plot the error 
plt.figure(figsize=(25,10))
for N in range(0,7):
    plt.plot(x, taylorError(x, N), '-')

# Set up matplotlib environment
plt.title(r"Error in the Taylor Expansion Approximation of Sine", fontsize=12)
plt.xlim(-3*np.pi, 3*np.pi)
plt.xlabel(r'$x$')
plt.ylabel(r'$|sin(x)-f_N(x)|$')
plt.ylim(0,9)
plt.grid(True)

# Plot a log-log plot of the error
plt.figure(figsize=(25,10))
for N in range(0,4):
    plt.loglog(x, taylorError(x, N), '-')

# Set up matplotlib environment
plt.title("Error in the Taylor Expansion Approximation of Sine (log graph)", fontsize=12)
plt.xlim(0.2,2*np.pi)
plt.xlabel('$log(x)$')
plt.ylim(10e-15,10e3)
plt.ylabel(r'$\log(|\sin(x)-f_N(x)|)$')
plt.grid(True)
plt.show()   


