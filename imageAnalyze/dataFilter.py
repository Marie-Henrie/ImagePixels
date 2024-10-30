import re

def filter_pixel_dataFile(input_file, output_file, x_range=(0, 999), y_range=(0, 999)):
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            # Loop through each line in the input file
            for line in infile:
                # Use regex to match the pixel data pattern
                match = re.match(r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)", line)
                if match:
                    # Extract x, y values from the match
                    x = int(match.group(1))
                    y = int(match.group(2))

                    # Check if x and y are within the desired range
                    if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                        # Write the matching line to the output file
                        outfile.write(line)

    print(f"Filtered pixel data saved to {output_file}")

# This function will be called from other file
if __name__ == "__main__":
     # Call the function
    filter_pixel_dataFile('rgb_values.txt', 'filtered_pixels_1000_1000.txt', x_range=(0, 999), y_range=(0, 999))
