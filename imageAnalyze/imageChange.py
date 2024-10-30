from PIL import Image

def apply_green_tint(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # COnvert the image to RGB
        img = img.convert("RGB")
        
        # Get the image dimensions
        width, height = img.size
        
        # Get the pixxels
        pixels = list(img.getdata())
        
        # Change the RGB values to green
        green_pixels = [(r//2, g, b//2) for r, g, b in pixels]  # change the Red and Blue values to less
        
        # Create the new image
        img.putdata(green_pixels)
        
        # Save the image
        img.save(output_path)
        print(f"Image with green tint saved at: {output_path}")

# This function will be called from other file
if __name__ == "__main__":
    # Call the function
    apply_green_tint(
    "images/cow.jpg", 
    "greenCow.jpg"
)
