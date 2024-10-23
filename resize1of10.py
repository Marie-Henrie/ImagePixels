from PIL import Image

def resize_image_quarter_pixels(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get original dimensions
        width, height = img.size
        print(f"Original size: {width}x{height}")
        
        # Calculate new dimensions to have 1/10th the total pixels (half width and height)
        new_width = width // 10
        new_height = height // 10
        
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        
        # Save the resized image to the output path
        resized_img.save(output_path)
        print(f"Resized image saved as {output_path} with size: {new_width}x{new_height}")
        print(f"New size has 1/4th the pixels of the original image.")

# Example usage:
resize_image_quarter_pixels("images/lehma.jpg", "output_resized_image_quarter_pixels.jpg")
