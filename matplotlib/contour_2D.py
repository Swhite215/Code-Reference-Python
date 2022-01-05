import numpy as np
import matplotlib.pyplot as plt

# Return evenly spaced numbers over a specified interval
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)

# Return coordinate matrices from coordinate vectors
X, Y = np.meshgrid(xlist, ylist)

# Return non-negative square root of an array, element wise
Z = np.sqrt(X**2 + Y**2)

# Create a figure and a set of subplots
fig,ax=plt.subplots(1,1)

# Plots contour lines
cp = ax.contourf(X, Y, Z)

# Add a colorbar to a plot
fig.colorbar(cp)

# Set Title
ax.set_title('Filled Contours Plot')

# Set Labels
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')

# Display Plot
plt.show()