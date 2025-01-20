import tkinter as tk
from tkinter import ttk
from PIL import Image
import numpy as np

# Updated color_tones dictionary with rearranged tones
color_tones = {
    'RED': {'rgb': (255, 0, 0), 'frequency': 391.3, 'tone': 'G', 'difference': 0.7},
    'Red Darker': {'rgb': (150, 0, 0), 'tone': 'G1'},  # Darker shade
    'Red Dark': {'rgb': (200, 0, 0), 'tone': 'G2'},   # Dark shade
    'Red Light': {'rgb': (255, 100, 100), 'tone': 'G3'},  # Light shade
    
    'REDDISH ORANGE': {'rgb': (255, 165, 0), 'frequency': 418.6, 'tone': 'G#', 'difference': 3.6},
    'Reddish Orange Darker': {'rgb': (150, 100, 0), 'tone': 'G#1'},  # Darker shade
    'Reddish Orange Dark': {'rgb': (200, 130, 0), 'tone': 'G#2'},   # Dark shade
    'Reddish Orange Light': {'rgb': (255, 180, 100), 'tone': 'G#3'},  # Light shade

    'ORANGE': {'rgb': (255, 255, 0), 'frequency': 445.9, 'tone': 'A', 'difference': 5.9},
    'Orange Darker': {'rgb': (150, 150, 0), 'tone': 'A1'},  # Darker shade
    'Orange Dark': {'rgb': (200, 200, 0), 'tone': 'A2'},   # Dark shade
    'Orange Light': {'rgb': (255, 255, 100), 'tone': 'A3'},  # Light shade
    
    'YELLOW': {'rgb': (255, 255, 51), 'frequency': 473.2, 'tone': 'A#', 'difference': 7.2},
    'Yellow Darker': {'rgb': (150, 150, 25), 'tone': 'A#1'},  # Darker shade
    'Yellow Dark': {'rgb': (200, 200, 25), 'tone': 'A#2'},   # Dark shade
    'Yellow Light': {'rgb': (255, 255, 100), 'tone': 'A#3'},  # Light shade

    'LEMON YELLOW': {'rgb': (255, 255, 102), 'frequency': 500.5, 'tone': 'B', 'difference': 6.5},
    'Lemon Yellow Darker': {'rgb': (150, 150, 50), 'tone': 'B1'},  # Darker shade
    'Lemon Yellow Dark': {'rgb': (200, 200, 50), 'tone': 'B2'},   # Dark shade
    'Lemon Yellow Light': {'rgb': (255, 255, 150), 'tone': 'B3'},  # Light shade

    'GREEN': {'rgb': (0, 255, 0), 'frequency': 527.8, 'tone': 'C', 'difference': 3.8},
    'Green Darker': {'rgb': (0, 150, 0), 'tone': 'C1'},  # Darker shade
    'Green Dark': {'rgb': (0, 200, 0), 'tone': 'C2'},   # Dark shade
    'Green Light': {'rgb': (100, 255, 100), 'tone': 'C3'},  # Light shade

    'TURQUOISE': {'rgb': (64, 224, 208), 'frequency': 555.1, 'tone': 'C#', 'difference': 0.1},
    'Turquoise Darker': {'rgb': (30, 140, 140), 'tone': 'C#1'},  # Darker shade
    'Turquoise Dark': {'rgb': (50, 180, 180), 'tone': 'C#2'},   # Dark shade
    'Turquoise Light': {'rgb': (100, 255, 255), 'tone': 'C#3'},  # Light shade

    'BLUE': {'rgb': (0, 0, 255), 'frequency': 582.3, 'tone': 'D', 'difference': 5.7},
    'Blue Darker': {'rgb': (0, 0, 150), 'tone': 'D1'},  # Darker shade
    'Blue Dark': {'rgb': (0, 0, 200), 'tone': 'D2'},   # Dark shade
    'Blue Light': {'rgb': (100, 100, 255), 'tone': 'D3'},  # Light shade

    'INDIGO': {'rgb': (75, 0, 130), 'frequency': 618.7, 'tone': 'D#', 'difference': 4.4},
    'Indigo Darker': {'rgb': (30, 0, 75), 'tone': 'D#1'},  # Darker shade
    'Indigo Dark': {'rgb': (50, 0, 100), 'tone': 'D#2'},   # Dark shade
    'Indigo Light': {'rgb': (100, 50, 180), 'tone': 'D#3'},  # Light shade

    'DARK VIOLET': {'rgb': (148, 0, 211), 'frequency': 655.1, 'tone': 'E', 'difference': 13.9},
    'Dark Violet Darker': {'rgb': (80, 0, 120), 'tone': 'E1'},  # Darker shade
    'Dark Violet Dark': {'rgb': (100, 0, 150), 'tone': 'E2'},   # Dark shade
    'Dark Violet Light': {'rgb': (180, 50, 255), 'tone': 'E3'},  # Light shade

    'DARKER VIOLET': {'rgb': (128, 0, 128), 'frequency': 691.5, 'tone': 'F', 'difference': 8.5},
    'Darker Violet Darker': {'rgb': (80, 0, 80), 'tone': 'F1'},  # Darker shade
    'Darker Violet Dark': {'rgb': (100, 0, 100), 'tone': 'F2'},   # Dark shade
    'Darker Violet Light': {'rgb': (160, 50, 160), 'tone': 'F3'},  # Light shade

    'ULTRA VIOLET': {'rgb': (238, 130, 238), 'frequency': 727.9, 'tone': 'F#', 'difference': 14.139},
    'Ultra Violet Darker': {'rgb': (180, 80, 180), 'tone': 'F#1'},  # Darker shade
    'Ultra Violet Dark': {'rgb': (200, 100, 200), 'tone': 'F#2'},   # Dark shade
    'Ultra Violet Light': {'rgb': (255, 150, 255), 'tone': 'F#3'},  # Light shade
}

# Function to calculate the Euclidean distance between two RGB colors
def color_distance(rgb1, rgb2):
    return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(rgb1, rgb2)))

# Function to find the closest color and its properties
def find_closest_color(avg_color):
    closest_color = None
    min_distance = float('inf')
    
    for color_name, properties in color_tones.items():
        distance = color_distance(avg_color, properties['rgb'])
        if distance < min_distance:
            min_distance = distance
            closest_color = (color_name, properties['tone'])
            
    return closest_color

# Load the image
image = Image.open('images/new_cat.jpg')
image = image.convert('RGB')
width, height = image.size
block_size = 23  # Size of each pixel block for analysis
output_image = Image.new('RGB', (width, height))

# Tkinter setup
root = tk.Tk()
root.title("Color Tone Adjuster")

# Adding a canvas for scrollable frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Dictionary to hold color preview labels
color_label = {}

# UI for each color in color_tones inside scrollable_frame
for idx, color_name in enumerate(color_tones):
    color_frame = tk.Frame(scrollable_frame)
    color_frame.pack(pady=5, fill="x", expand=True)

    tk.Label(color_frame, text=color_name).grid(row=0, column=0, columnspan=3)

    # Sliders for RGB values (code omitted here for brevity, same as original)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Process image blocks and update output image
def process_image_blocks():
    # Dynamically determine table dimensions based on image size
    num_rows = height // block_size
    num_cols = width // block_size
    tone_table = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    with open('data/color_data_rgb_cat.txt', 'w') as file:
        for row in range(num_rows):
            for col in range(num_cols):
                # Calculate block position
                x = col * block_size
                y = row * block_size
                
                # Crop the image to get the current block
                box = (x, y, min(x + block_size, width), min(y + block_size, height))
                block = image.crop(box)
                block_np = np.array(block)
                avg_color = block_np.mean(axis=(0, 1)).astype(int)  # Average color
                avg_color_tuple = tuple(avg_color)

                # Find the closest color for the average color
                closest_color_info = find_closest_color(avg_color_tuple)

                # Save the RGB values, closest color name, and tone to the text file
                file.write(f"Block at ({x}, {y}) - Avg Color: {avg_color_tuple[0]}, {avg_color_tuple[1]},{avg_color_tuple[2]} - Closest Color: {closest_color_info[0]}, Tone: {closest_color_info[1]}\n")
                
                # Store the closest tone in the table at (row, col)
                tone_table[row][col] = closest_color_info[1] if closest_color_info else ""
                
                # Create a block with the average color for output
                color_block = Image.new('RGB', (box[2] - box[0], box[3] - box[1]), avg_color_tuple)
                output_image.paste(color_block, box)

    # Save the output image
    output_image.save('images/output_color_blocks_cat.jpg')
    print("Processing complete. Check 'color_data_rgb_cat.txt' and 'output_color_blocks_cat.jpg'.")

    # Print the tone table
    print("\nTone Table:")
    for row in tone_table:
        print(" | ".join(row))

# Add a button to process image blocks
process_button = tk.Button(root, text="Process Image Blocks", command=process_image_blocks)
process_button.pack(pady=20)

root.mainloop()
