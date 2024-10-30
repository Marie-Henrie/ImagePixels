import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# This function analyze the pixeldata.txt and create red, green and blue channels. THen create the image again to show on screen.

# Step 1: Read and Parse the File
filename = 'data/imagesToPixels_cow.txt'  # Update with the actual path to your file

# Read and extract pixel data using regular expressions
with open(filename, 'r') as file:
    data = file.read()

# Regular expression to extract x, y, R, G, B values
pattern = r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)"
matches = re.findall(pattern, data)

# Convert to DataFrame
pixels = pd.DataFrame(matches, columns=['x', 'y', 'R', 'G', 'B']).astype(int)

# Step 2: Create RGB Matrices
# Initialize matrices for RGB values
img_R = np.zeros((288, 288), dtype=int)
img_G = np.zeros((288, 288), dtype=int)
img_B = np.zeros((288, 288), dtype=int)

# Populate matrices with the pixel RGB values
for _, row in pixels.iterrows():
    img_R[row['y'], row['x']] = row['R']
    img_G[row['y'], row['x']] = row['G']
    img_B[row['y'], row['x']] = row['B']

# Step 3: Visualize the RGB Channels
# Plot Red Channel
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(img_R, cmap='Reds')
plt.colorbar()
plt.title('Red Channel')

# Plot Green Channel
plt.subplot(1, 3, 2)
plt.imshow(img_G, cmap='Greens')
plt.colorbar()
plt.title('Green Channel')

# Plot Blue Channel
plt.subplot(1, 3, 3)
plt.imshow(img_B, cmap='Blues')
plt.colorbar()
plt.title('Blue Channel')

plt.tight_layout()
plt.show()

# Step 4: Display Reconstructed Image
# Stack RGB channels into a single image array and normalize values
img_rgb = np.dstack((img_R, img_G, img_B)) / 255.0

# Display the reconstructed image
plt.figure(figsize=(6, 6))
plt.imshow(img_rgb)
plt.title('Reconstructed Image')
plt.axis('off')
plt.show()
