from PIL import Image
import math

def resize_image_half_pixels(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get original dimensions
        width, height = img.size
        print(f"Original size: {width}x{height}")
        
        # Calculate new dimensions to have half the total pixels
        factor = math.sqrt(2)
        new_width = int(width / factor)
        new_height = int(height / factor)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        
        # Save the resized image to the output path
        resized_img.save(output_path)
        print(f"Resized image saved as {output_path} with size: {new_width}x{new_height}")
        print(f"New size has approximately half the pixels of the original image.")

# Example usage:
resize_image_half_pixels("images/lehma.jpg", "output_resized_image_half_pixels.jpg")

