from PIL import Image

# This funciton open the image and analyse the pixels colors and save the data to a new file

def save_image_pixels_toFile(image_path, rgb_output_file):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB if it's not already
        img = img.convert("RGB")
        
        # Get the image data as bytes (pixel values in (R, G, B) format)
        pixels = list(img.getdata())
        
        # Get image dimensions
        width, height = img.size
        
        # Store RGB values for the entire image
        rgb_values = []
        
        # Print and store RGB values for the first 1 row, starting with row number 0
        print("First row of RGB values of the image:")
        for y in range(min(1, height)):  # Only loop through the first row
            row_rgb = []
            for x in range(width):
                index = y * width + x
                r, g, b = pixels[index]
                row_rgb.append((r, g, b))
                print(f"Pixel ({x}, {y}): (R: {r}, G: {g}, B: {b})")
            rgb_values.append(row_rgb)

        # Save all RGB values to a file
        with open(rgb_output_file, 'w') as f:
            for y in range(height):
                for x in range(width):
                    index = y * width + x
                    r, g, b = pixels[index]
                    f.write(f"Pixel ({x}, {y}): (R: {r}, G: {g}, B: {b})\n")
        
        print(f"\nRGB values are saved to: {rgb_output_file}")
        

# This function will be called from other file
if __name__ == "__main__":
    # Call the function and save the RGB data to a .txt file
    save_image_pixels_toFile("images/mosaic_image.jpg", "imagesToPixels_cow.txt")
