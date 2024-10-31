import CreateImage
import dataFilter
import imageChange
import ImagetoFile
import resize1of10
import resizeImage

# Define the functions for the different options

def option_one():
    print("You selected option 1: Create an image.")
    CreateImage.create_image_from_rgb_file('imagesPixels.txt', 'rebuilt_Cat1.png')

def option_two():
    print("You selected option 2: Filter data for 1000 rows only.")
    dataFilter.filter_pixel_dataFile('rgb_values.txt', 'filtered_pixels_1000_1000.txt', x_range=(0, 999), y_range=(0, 999))


def option_three():
    print("You selected option 3: Add the green firter to an image.")
    imageChange.apply_green_tint("images/cow.jpg", "greenCow.jpg")

def option_four():
    print("You selected option 4: Save the image data to a file.")
    ImagetoFile.save_image_pixels_toFile("images/new_cat.jpg", "imagesPixels.txt")

def option_five():
    print("You selected option 5: Resize the image 1 of 10th of the original size.")
    resize1of10.resize_image_pixels("images/cat.jpg", "images/new_Cat.jpg")

def option_six():
    print("You selected option 3: Resize the image in half size.")
    resizeImage.resize_image_half_size("Images/cow.jpg", "Images/newImageHalfSize2.jpg")


def option_seven():
    print("You selected option 7: Exit the program.")
    print("Have a nice day!")
    exit()  # Exit the program


# Main program function to show the list option
def main_program():
    while True:
        print("Please select an option from the list:")
        print("1. Create an image")
        print("2. Filter data for 1000 rows only")
        print("3. Add the green firter to an image")
        print("4. Save the image data to a file.")
        print("5. Resize the image 1 of 10th of the original size")
        print("6. Resize the image in half size")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            option_one()
        elif choice == '2':
            option_two()
        elif choice == '3':
            option_three()
        elif choice == '4':
            option_four()
        elif choice == '5':
            option_five()
        elif choice == '6':
            option_six()
        elif choice == '7':
            option_seven()
        else:
            print("Invalid choice, please enter a number between 1 and 7.\n")


# Run the main program
if __name__ == "__main__":
    main_program()
