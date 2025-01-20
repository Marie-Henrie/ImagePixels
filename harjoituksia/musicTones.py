from PIL import Image
import numpy as np

# Define the RGB values and properties for the tones based on your table
color_tones = {
    'Red': {'rgb': (255, 0, 0), 'frequency': 391.3, 'tone': 'G', 'difference': 0.7},
    'Reddish Orange': {'rgb': (255, 165, 0), 'frequency': 418.6, 'tone': 'G#', 'difference': 3.6},
    'Orange': {'rgb': (255, 255, 0), 'frequency': 445.9, 'tone': 'A', 'difference': 5.9},
    'Yellow': {'rgb': (255, 255, 51), 'frequency': 473.2, 'tone': 'A#', 'difference': 7.2},
    'Lemon Yellow': {'rgb': (255, 255, 102), 'frequency': 500.5, 'tone': 'H/B', 'difference': 6.5},
    'Green': {'rgb': (0, 255, 0), 'frequency': 527.8, 'tone': 'C', 'difference': 3.8},
    'Turquoise': {'rgb': (64, 224, 208), 'frequency': 555.1, 'tone': 'C#', 'difference': 0.1},
    'Blue': {'rgb': (0, 0, 255), 'frequency': 582.3, 'tone': 'D', 'difference': 5.7},
    'Indigo': {'rgb': (75, 0, 130), 'frequency': 618.7, 'tone': 'D#', 'difference': 4.4},
    'Dark Violet': {'rgb': (148, 0, 211), 'frequency': 655.1, 'tone': 'E', 'difference': 13.9},
    'Darker Violet': {'rgb': (128, 0, 128), 'frequency': 691.5, 'tone': 'F', 'difference': 8.5},
    'Ultra Violet': {'rgb': (238, 130, 238), 'frequency': 727.9, 'tone': 'F#', 'difference': 14.139}
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
            closest_color = (color_name, properties['tone'])  # Return color name and tone
            
    return closest_color

# Function to print color blocks and RGB values in the terminal
def print_color_block_with_text(avg_color, position, color_info):
    color_name, tone = color_info
    r, g, b = avg_color
    # Print colored block using ANSI escape codes, followed by the RGB values and color information
    print(f"\033[48;2;{r};{g};{b}m  \033[0m Block at {position} - Average Color: {r},{g},{b} - Closest Color: {color_name}, Tone: {tone}")

# Load the image
image = Image.open('images/new_Cow.jpg')

# Convert the image to RGB mode (if not already)
image = image.convert('RGB')

# Get image dimensions
width, height = image.size

# Size of each block
block_size = 32

# Create a new blank image for the output
output_image = Image.new('RGB', (width, height))

# Open the file to save RGB color data
with open('color_data_rgb.txt', 'w') as file:
    # Iterate over the image in blocks
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            # Define the region (block) coordinates
            box = (x, y, min(x + block_size, width), min(y + block_size, height))
            
            # Crop the block from the image
            block = image.crop(box)
            
            # Convert the block to a numpy array
            block_np = np.array(block)
            
            # Calculate the average color of the block
            avg_color = block_np.mean(axis=(0, 1)).astype(int)  # Mean along width and height
            avg_color_tuple = tuple(avg_color)
            
            # Find the closest color for the average color
            closest_color_info = find_closest_color(avg_color_tuple)
            
            # Print the average color block with text in the terminal
            print_color_block_with_text(avg_color_tuple, (x, y), closest_color_info)
            
            # Save the RGB values, closest color name, and tone to the text file
            file.write(f"Block at ({x}, {y}) - Average Color: {avg_color_tuple[0]},{avg_color_tuple[1]},{avg_color_tuple[2]} - Closest Color: {closest_color_info[0]}, Tone: {closest_color_info[1]}\n")
            
            # Create a block with the average color
            color_block = Image.new('RGB', (box[2] - box[0], box[3] - box[1]), avg_color_tuple)
            
            # Paste the color block into the output image
            output_image.paste(color_block, (x, y))
        
        # Move to the next line in the terminal after each row
        print()

# Save the output image
output_image.save('mosaic_image.jpg')
output_image.show()

print("\nRGB image saved to 'mosaic_image.jpg'.")
print("\nRGB color data with block information saved to 'color_data_rgb.txt'.")
