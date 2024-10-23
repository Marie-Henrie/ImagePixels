import matplotlib.pyplot as plt

# Data for the plot (X and Y values)
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create the plot
plt.plot(x, y, label='y = x^2', marker='o')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot: y = x^2')

# Add a legend
plt.legend()

# Display the plot
plt.show()
