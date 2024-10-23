from PIL import Image

def modify_pixel_and_apply_green_tint(image_path, output_path, rgb_output_file, pixel_x, pixel_y, new_rgb):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB if it's not already
        img = img.convert("RGB")
        
        # Get the image data as bytes (pixel values in (R, G, B) format)
        pixels = list(img.getdata())
        
        # Get image dimensions
        width, height = img.size
        
        # Store RGB values
        rgb_values = []

        # Print and store RGB values for the first 10 rows
        print("First 10 rows of RGB values of the image:")
        for y in range(min(10, height)):
            row_rgb = []
            for x in range(width):
                index = y * width + x
                r, g, b = pixels[index]
                row_rgb.append((r, g, b))
                print(f"Pixel ({x}, {y}): (R: {r}, G: {g}, B: {b})")
            rgb_values.append(row_rgb)
        
        # Save RGB values to a file
        with open(rgb_output_file, 'w') as f:
            for y in range(min(10, height)):
                for x in range(width):
                    r, g, b = rgb_values[y][x]
                    f.write(f"Pixel ({x}, {y}): (R: {r}, G: {g}, B: {b})\n")
        
        # Print how many pixels are in each row
        print(f"\nNumber of pixels in each row: {width}")
        
        # Check if the pixel coordinates are within the image dimensions
        if 0 <= pixel_x < width and 0 <= pixel_y < height:
            # Modify the specified pixel with the new RGB value
            index = pixel_y * width + pixel_x
            pixels[index] = new_rgb  # Set new RGB value
            
            # Apply the green tint by modifying the pixel values
            green_pixels = [(255, 255, 255) if (r, g, b) != new_rgb else new_rgb for (r, g, b) in pixels]
            
            # Now modify a 100x100 pixel square to black, ensuring it fits within image dimensions
            square_size = 100
            for y in range(pixel_y, min(pixel_y + square_size, height)):
                for x in range(pixel_x, min(pixel_x + square_size, width)):
                    index = y * width + x
                    green_pixels[index] = (0, 0, r)  # Set to black
        
            # Create a new image with the modified pixels
            img.putdata(green_pixels)
        else:
            print(f"Pixel coordinates ({pixel_x}, {pixel_y}) are out of bounds.")
            return
        
        # Save the modified image to the output path
        img.save(output_path)
        print(f"\nImage with modified pixel saved at: {output_path}")
        print(f"RGB values saved at: {rgb_output_file}")

# Example usage:
modify_pixel_and_apply_green_tint("images/lehma.jpg", "output_modified_image.jpg", "rgb_values.txt", pixel_x=1, pixel_y=1, new_rgb=(0, 0, 0))  # Change pixel at (1, 1) and 100x100 square to black
