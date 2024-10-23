from PIL import Image

def resize_image_pixels(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get othe riginal dimensions
        width, height = img.size
        print(f"Original size is: {width}x{height}")
        
        # Calculate new dimensions to have 1/10th the total pixels
        new_width = width // 10
        new_height = height // 10
        
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        
        # Save the resized image to the output path
        resized_img.save(output_path)
        print(f"Resized image saved as {output_path} with size: {new_width}x{new_height}")
        print(f"New size has 1/10th the pixels of the original image.")

# Call the function:
resize_image_pixels("images/lehma.jpg", "images/new_Cow.jpg")
