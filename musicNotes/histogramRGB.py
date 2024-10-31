import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read and Parse the File
filename = 'imagesPixels.txt'  # Update with the actual path to your file

# Read and extract pixel data using regular expressions
with open(filename, 'r') as file:
    data = file.read()

# Regular expression to extract x, y, R, G, B values
pattern = r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)"
matches = re.findall(pattern, data)

# Convert to DataFrame
pixels = pd.DataFrame(matches, columns=['x', 'y', 'R', 'G', 'B']).astype(int)

# Step 2: Calculate Average RGB Values
avg_R = pixels['R'].mean()
avg_G = pixels['G'].mean()
avg_B = pixels['B'].mean()

# Step 3: Plot the Average RGB Values as a Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(['Red', 'Green', 'Blue'], [avg_R, avg_G, avg_B], color=['red', 'green', 'blue'])
plt.ylabel('Average Intensity')
plt.title('Average RGB Values')
plt.show()

# Step 4: Plot Histogram of RGB Values
plt.figure(figsize=(15, 5))

# Red channel histogram
plt.subplot(1, 3, 1)
plt.hist(pixels['R'], bins=25, color='red', alpha=0.7)
plt.xlabel('Red Intensity')
plt.ylabel('Frequency')
plt.title('Red Channel Intensity Distribution')

# Green channel histogram
plt.subplot(1, 3, 2)
plt.hist(pixels['G'], bins=25, color='green', alpha=0.7)
plt.xlabel('Green Intensity')
plt.ylabel('Frequency')
plt.title('Green Channel Intensity Distribution')

# Blue channel histogram
plt.subplot(1, 3, 3)
plt.hist(pixels['B'], bins=25, color='blue', alpha=0.7)
plt.xlabel('Blue Intensity')
plt.ylabel('Frequency')
plt.title('Blue Channel Intensity Distribution')

plt.tight_layout()
plt.show()
