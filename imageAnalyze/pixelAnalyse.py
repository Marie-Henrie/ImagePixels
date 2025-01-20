import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# This function analyze the txt file and create red, green and blue channels. THen create the image again to show on screen.
def create_RGB_analyse(input_file):
    # Step 1: Read and Parse the File
    #filename = 'data/imagesToPixels_cow.txt'  # Update with the actual path to your file

    # Read and extract pixel data using regular expressions
    with open(input_file, 'r') as file:
        data = file.read()

    # Regular expression to extract x, y, R, G, B values
    pattern = r"Pixel \((\d+), (\d+)\): \(R: (\d+), G: (\d+), B: (\d+)\)"
    matches = re.findall(pattern, data)

    # Convert to DataFrame
    pixels = pd.DataFrame(matches, columns=['x', 'y', 'R', 'G', 'B']).astype(int)

    # Step 2: Create RGB Matrices and analyse the picture height and weight automatic

    image_width = pixels['x'].max() + 1 # Width is the maximum x-coordinate + 1
    image_height = pixels['y'].max() + 1 # Height is the maximum y-coordinate + 1

    # Initialize matrices for RGB values
    img_R = np.zeros((image_height, image_width), dtype=int)
    img_G = np.zeros((image_height, image_width), dtype=int)
    img_B = np.zeros((image_height, image_width), dtype=int)

    # Populate matrices with the pixel RGB values
    for _, row in pixels.iterrows():
        img_R[row['y'], row['x']] = row['R']
        img_G[row['y'], row['x']] = row['G']
        img_B[row['y'], row['x']] = row['B']

    # Step 3: Visualize the RGB Channels
    # Plot Red Channel
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img_R, cmap='Reds')
    plt.colorbar()
    plt.title('Red Channel')

    # Plot Green Channel
    plt.subplot(1, 3, 2)
    plt.imshow(img_G, cmap='Greens')
    plt.colorbar()
    plt.title('Green Channel')

    # Plot Blue Channel
    plt.subplot(1, 3, 3)
    plt.imshow(img_B, cmap='Blues')
    plt.colorbar()
    plt.title('Blue Channel')

    plt.tight_layout()
    plt.show()

    # Step 4: Display Reconstructed Image
    # Stack RGB channels into a single image array and normalize values
    img_rgb = np.dstack((img_R, img_G, img_B)) / 255.0

    # Display the reconstructed image
    plt.figure(figsize=(6, 6))
    plt.imshow(img_rgb)
    plt.title('Reconstructed Image')
    plt.axis('off')
    plt.show()
