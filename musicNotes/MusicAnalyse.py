import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read and Parse the File
filename = 'imagesToPixels.txt'  # Update with the actual path to your file

# Read and extract pixel data using regular expressions
with open(filename, 'r') as file:
    data = file.read()

# Regular expression to extract x, y, R, G, B values
pattern = r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)"
matches = re.findall(pattern, data)

# Convert to DataFrame
pixels = pd.DataFrame(matches, columns=['x', 'y', 'R', 'G', 'B']).astype(int)

# Step 2: Map RGB values to Musical Notes
note_mapping = {
    'C': 0,    # Green hue (high G value)
    'G': 1,    # Red hue (high R value)
    'F': 2     # Blue hue (high B value)
}

# Initialize counts for each note
note_counts = {'C': 0, 'G': 0, 'F': 0}

# Thresholds for color mapping
green_threshold = 150
red_threshold = 150
blue_threshold = 150

# Analyze each pixel's RGB value
for _, row in pixels.iterrows():
    R, G, B = row['R'], row['G'], row['B']
    if G >= green_threshold and R < red_threshold and B < blue_threshold:
        note_counts['C'] += 1
    elif R >= red_threshold and G < green_threshold and B < blue_threshold:
        note_counts['G'] += 1
    elif B >= blue_threshold and R < red_threshold and G < green_threshold:
        note_counts['F'] += 1

# Step 3: Visualize the Note Counts
notes = list(note_counts.keys())
counts = list(note_counts.values())

plt.figure(figsize=(8, 6))
plt.bar(notes, counts, color=['green', 'red', 'blue'])
plt.ylabel('Note Count')
plt.title('Musical Notes Distribution Based on RGB Values')
plt.show()
