import tkinter as tk
from tkinter import filedialog, messagebox
import ResizeImage
import resize1of10
import ImagetoFile
import DataFilter
import CreateImage
import HistogramRGB
import PixelAnalyse
import ImageSplitAndMosaic
from tkinter import simpledialog





# Toimintojen määrittely

def resize_image_half():
    input_image = filedialog.askopenfilename(title="Select the image file")
    output_image = filedialog.asksaveasfilename(title="Save the resized image as", defaultextension=".jpg")
    if input_image and output_image:
        ResizeImage.resize_image_half_size(input_image, output_image)
        messagebox.showinfo("Success", f"Resized image saved as {output_image}")

def resize_image_tenth():
    input_image = filedialog.askopenfilename(title="Select the image file")
    output_image = filedialog.asksaveasfilename(title="Save the resized image as", defaultextension=".jpg")
    if input_image and output_image:
        resize1of10.resize_image_pixels(input_image, output_image)
        messagebox.showinfo("Success", f"Resized image saved as {output_image}")      

def save_image_data():
    input_image = filedialog.askopenfilename(title="Select the image file")
    output_file = filedialog.asksaveasfilename(title="Save the image data as", defaultextension=".txt")
    if input_image and output_file:
        ImagetoFile.save_image_pixels_toFile(input_image, output_file)
        messagebox.showinfo("Success", f"Image data saved as {output_file}")  

def filter_data():
    input_file = filedialog.askopenfilename(title="Select the RGB text file")
    output_file = filedialog.asksaveasfilename(title="Save the filtered data as", defaultextension=".txt")
    if input_file and output_file:
        DataFilter.filter_pixel_dataFile(input_file, output_file, x_range=(0, 999), y_range=(0, 999))
        messagebox.showinfo("Success", f"Filtered data saved as {output_file}")

def create_image():
    input_file = filedialog.askopenfilename(title="Select the RGB text file")
    output_file = filedialog.asksaveasfilename(title="Save the rebuilt image as", defaultextension=".png")
    if input_file and output_file:
        CreateImage.create_image_from_rgb_file(input_file, output_file)
        messagebox.showinfo("Success", f"Image created and saved as {output_file}")

def create_HistogramRGB():
    input_file = filedialog.askopenfilename(title="Select the text file")
    if input_file:
        try:
            HistogramRGB.create_HistogramRGB(input_file)
            messagebox.showinfo("Success", f"Histogram created successfully for {input_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def create_RGB_analyse():
    input_file = filedialog.askopenfilename(title="Select the text file")
    if input_file:
        try:
            PixelAnalyse.create_RGB_analyse(input_file)
            messagebox.showinfo("Success", f"RBG analyse created successfully for {input_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_mosaic():
    # Ask user to select input image file
    input_file = filedialog.askopenfilename(title="Select the input image file")
    if not input_file:
        messagebox.showwarning("No File Selected", "Please select an input file.")
        return

    # Ask user for output image file name
    output_image_file = filedialog.asksaveasfilename(title="Save the mosaic image as", defaultextension=".jpg")
    if not output_image_file:
        messagebox.showwarning("No File Selected", "Please select a file to save the mosaic image.")
        return

    # Ask user for output text file name
    output_text_file = filedialog.asksaveasfilename(title="Save the RGB data as", defaultextension=".txt")
    if not output_text_file:
        messagebox.showwarning("No File Selected", "Please select a file to save the RGB data.")
        return

    # Ask user for block size
    try:
        block_size = simpledialog.askinteger("Block Size", "Enter the size of each block (e.g., 35):", minvalue=1)
        if not block_size:
            messagebox.showwarning("Invalid Input", "Block size must be a positive integer.")
            return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while setting block size: {str(e)}")
        return
    
    try:
        # Call the create_mosaic function with all arguments
        ImageSplitAndMosaic.create_mosaic(input_file, output_image_file, output_text_file, block_size)
        messagebox.showinfo("Success", "RGB analysis and mosaic image created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def create_tones_modifier():
    input_file = filedialog.askopenfilename(title="Select the text file")
    if input_file:
        try:
            PixelAnalyse.create_RGB_analyse(input_file)
            messagebox.showinfo("Success", f"RBG analyse created successfully for {input_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def exit_program():
    root.destroy()

# Tkinter-pääikkuna
root = tk.Tk()
root.title("Image Processing Tool")
root.geometry("600x600")

# Otsikko
title_label = tk.Label(root, text="Image Processing Tool", font=("Arial", 16))
title_label.pack(pady=10)

# Painikkeet
buttons = [
    ("Resize Image (Half Size)", resize_image_half),
    ("Resize Image (1/10th)", resize_image_tenth),
    ("Save Image Data to File", save_image_data),
    ("Filter Data (1000 rows)", filter_data),  
    ("Create an Image from text file", create_image),
    ("Create an Histrogram from text file", create_HistogramRGB),
    ("Create an RGB analyse from text file", create_RGB_analyse),
    ("Create an Mosaic from a picture", create_mosaic),
    ("Exit", exit_program)
]

for text, command in buttons:
    button = tk.Button(root, text=text, command=command, width=30, pady=5)
    button.pack(pady=5)

# Käynnistetään Tkinter-looppi
root.mainloop()
