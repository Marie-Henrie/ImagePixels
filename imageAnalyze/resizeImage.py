from PIL import Image
import math

def resize_image_half_size(image_path, output_path):
    # Open the image
    with Image.open(image_path) as pic:
        # Get original size
        width, height = pic.size
        print(f"Original size: {width}x{height}")
        
        # Calculate new size
        squareRoot = math.sqrt(2)
        new_width = int(width / squareRoot)
        new_height = int(height / squareRoot)
        
        # Resize the image
        resized_pic = pic.resize((new_width, new_height))
        
        # Save the resized image to the output path
        resized_pic.save(output_path)
        print(f"Resized image saved as {output_path} with size: {new_width}x{new_height}")
        
# This function will be called from other file
if __name__ == "__main__":
    # Call the function, change here the picture path
    resize_image_half_size("Images/cow.jpg", "Images/newImageHalfSize2.jpg")

