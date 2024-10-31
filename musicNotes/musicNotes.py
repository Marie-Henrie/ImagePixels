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

# Step 4: Draw the Music Staff and Notes
def draw_staff(ax):
    """Draw the five lines of a music staff."""
    for i in range(5):
        ax.hlines(y=i, xmin=0, xmax=3, color='black', lw=2)

def draw_note_on_staff(ax, note, line_index):
    """Draw a simple representation of a musical note on the staff."""
    note_positions = {
        'C': 3,  # 3rd line
        'G': 2,  # 2nd line
        'F': 1   # 1st line
    }
    pos = note_positions[note]
    
    ax.annotate(note, xy=(1, pos + line_index * 0.2), fontsize=20, ha='center', va='center', color='black')
    ax.plot([1, 1], [pos + line_index * 0.2 - 0.1, pos + line_index * 0.2 - 0.5], color='black', lw=5)  # Note stem

# Create a new figure for drawing notes
plt.figure(figsize=(8, 4))
ax = plt.gca()
ax.set_xlim(0, 3)
ax.set_ylim(-1, 5)

# Draw the staff
draw_staff(ax)

# Draw notes based on counts
line_offset = 0  # Offset for lines to spread out notes vertically
for note, count in note_counts.items():
    for i in range(count):
        draw_note_on_staff(ax, note, line_offset)
        line_offset += 1  # Move up for the next note

ax.axis('off')  # Hide axes
plt.title('Musical Notes on Staff')
plt.show()
