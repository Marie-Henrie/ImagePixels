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

    'LEMON YELLOW': {'rgb': (255, 255, 102), 'frequency': 500.5, 'tone': 'H/B', 'difference': 6.5},
    'Lemon Yellow Darker': {'rgb': (150, 150, 50), 'tone': 'H/B1'},  # Darker shade
    'Lemon Yellow Dark': {'rgb': (200, 200, 50), 'tone': 'H/B2'},   # Dark shade
    'Lemon Yellow Light': {'rgb': (255, 255, 150), 'tone': 'H/B3'},  # Light shade

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

# Function to update color_tones with slider values
def update_color_tones(color_name, r, g, b):
    color_tones[color_name]['rgb'] = (r, g, b)
    update_color_preview(color_name)

# Function to display color preview for each tone
def update_color_preview(color_name):
    r, g, b = color_tones[color_name]['rgb']
    color_label[color_name].config(bg=f'#{r:02x}{g:02x}{b:02x}')

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

# Function to print color blocks and RGB values in the terminal
def print_color_block_with_text(avg_color, position, color_info):
    color_name, tone = color_info
    r, g, b = avg_color
    print(f"\nPosition: {position}, Closest Color: {color_name}, Tone: {tone}, RGB: ({r}, {g}, {b})")

# Function to save the updated colors to a file
def save_colors_to_file():
    with open("updated_colors.txt", "w") as f:
        for color_name, properties in color_tones.items():
            r, g, b = properties['rgb']
            f.write(f"{color_name}: {r}, {g}, {b}\n")
    print("Colors saved to updated_colors.txt")

# Create the main window
root = tk.Tk()
root.title("Color Tones Adjuster")
root.geometry("800x600")

# Create a frame for color controls
color_frame = tk.Frame(root)
color_frame.pack(pady=20)

# Create labels and sliders for each color tone
color_label = {}
for color_name in color_tones:
    frame = tk.Frame(color_frame)
    frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    label = tk.Label(frame, text=color_name)
    label.pack(side=tk.LEFT)

    r_slider = tk.Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL, label='R', command=lambda val, name=color_name: update_color_tones(name, int(val), color_tones[name]['rgb'][1], color_tones[name]['rgb'][2]))
    r_slider.set(color_tones[color_name]['rgb'][0])
    r_slider.pack(side=tk.LEFT, padx=5)

    g_slider = tk.Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL, label='G', command=lambda val, name=color_name: update_color_tones(name, color_tones[name]['rgb'][0], int(val), color_tones[name]['rgb'][2]))
    g_slider.set(color_tones[color_name]['rgb'][1])
    g_slider.pack(side=tk.LEFT, padx=5)

    b_slider = tk.Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL, label='B', command=lambda val, name=color_name: update_color_tones(name, color_tones[name]['rgb'][0], color_tones[name]['rgb'][1], int(val)))
    b_slider.set(color_tones[color_name]['rgb'][2])
    b_slider.pack(side=tk.LEFT, padx=5)

    color_label[color_name] = tk.Label(frame, width=10, height=2, bg=f'#{r_slider.get():02x}{g_slider.get():02x}{b_slider.get():02x}')
    color_label[color_name].pack(side=tk.LEFT, padx=5)

# Save button
save_button = tk.Button(root, text="Save Colors", command=save_colors_to_file)
save_button.pack(pady=20)

# Run the application
root.mainloop()
