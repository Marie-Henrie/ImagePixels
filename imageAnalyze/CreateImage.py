from PIL import Image
import re

# function create a new iamge based on text file, where is RGB values in lines
# the file have been created from original RGB image
def create_image_from_rgb_file(input_file, output_image):
    max_x, max_y = 0, 0

    # Analyse the image dimensions
    with open(input_file, 'r') as f:
        for line in f:
            match = re.match(r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)", line)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # Image dimensions are max_x + 1 and max_y + 1 (since coordinates start from 0)
    width = max_x + 1
    height = max_y + 1

    print(f"Image dimensions: Width = {width}, Height = {height}")

    # Create a new image from the txt file RBG values
    try:
        img = Image.new('RGB', (width, height), (255, 255, 255))  # Initialize with white background
    except MemoryError as e:
        print(f"Error: Not enough memory to create an image of size {width}x{height}")
        return

    # Set the pixels based on the RGB values in the file
    with open(input_file, 'r') as f:
        for line in f:
            match = re.match(r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)", line)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                r = int(match.group(3))
                g = int(match.group(4))
                b = int(match.group(5))
                
                # Set the pixel in the image at (x, y)
                if x < width and y < height:
                    img.putpixel((x, y), (r, g, b))

    # Save the image to the output path
    try:
        img.save(output_image)
        print(f"Image saved to {output_image}")
    except Exception as e:
        print(f"Error saving the image: {e}")

# This function will be called from other file
#if __name__ == "__main__":
    # Call the function and create the new image and save it
#    create_image_from_rgb_file('data/imagesToPixels_cow.txt', 'Pixel_Cow.png')
