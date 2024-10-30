from PIL import Image
import numpy as np

# This function build the image to color squares, and resize the image in a big scale. 
# It analyse the color squares and give the average color in rgb-value.


# Function to print color blocks and RGB values in the terminal
def print_color_block_with_text(avg_color, position):
    # Extract RGB values
    r, g, b = avg_color
    # Print colored block using ANSI escape codes, followed by the RGB values as text
    print(f"\033[48;2;{r};{g};{b}m  \033[0m Block at {position} - Average Color: {r},{g},{b}")

# Load the image
image = Image.open('images/new_rabbit.jpg')

# Convert the image to RGB mode (if not already)
image = image.convert('RGB')

# Get image dimensions
width, height = image.size

# Size of each block
block_size = 35

# Create a new blank image for the output
output_image = Image.new('RGB', (width, height))

# Open the file to save RGB color data
with open('color_data_rgb_rabbit.txt', 'w') as file:
    # Iterate over the image in 50x50 blocks
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
            
            # Print the average color block with text in the terminal
            print_color_block_with_text(avg_color_tuple, (x, y))
            
            # Save the RGB values to the text file with block position information
            file.write(f"Block at ({x}, {y}) - Average Color: {avg_color_tuple[0]},{avg_color_tuple[1]},{avg_color_tuple[2]}\n")
            
            # Create a block with the average color
            color_block = Image.new('RGB', (box[2] - box[0], box[3] - box[1]), avg_color_tuple)
            
            # Paste the color block into the output image
            output_image.paste(color_block, (x, y))
        
        # Move to the next line in the terminal after each row
        print()

# Save the output image
output_image.save('mosaic_rabbit.jpg')
output_image.show()

print("\nRGB image saved to 'mosaic_rabbit.jpg'.")
print("\nRGB color data with block information saved to 'color_data_rgb_rabbit.txt'.")
