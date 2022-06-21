# Dependencies
import cv2
import numpy as np
import argparse
 
 # General Character List
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

# Getting initialized data 
def get_data(user_choice):

    char_list= Character[user_choice.mode] # Character List; Default Mode = "Standard"
    num_chars = len(char_list) # length of character list
    num_cols = 150 # Number of character for output's width

    input= user_choice.input # Default input ="data/ascii_images/input.jpg"
    output = user_choice.output # Default output ="data/ascii_images/image_text.txt"

    return char_list, num_chars, num_cols, input, output

def main():

    # Getting data from get_data function
    char_list, num_chars, num_cols, input, output = get_data(user_choice)

    # Reading Input Image
    image = cv2.imread(input)

    # Converting Color Image to Grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extracting height and width from Image
    height, width = image.shape

    # Defining height and width of each cell==pixel
    cell_width = width / num_cols
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    
    # Output file
    output_file = open(output, 'w')

    # Mapping the Characters
    for i in range(num_rows):
        min_height = min(int((i + 1) * cell_height), height)
        row_pix = int(i * cell_height)

        for j in range(num_cols):
            output_file.write(
                char_list[min(int(np.mean(image[row_pix:min_height,
                                          int(j * cell_width):min(int((j + 1) * cell_width),
                                                                  width)]) * num_chars / 255), num_chars - 1)])
        output_file.write("\n")

    output_file.close()

# Utility function for parsing arguments
def get_args():

    parser = argparse.ArgumentParser("ASCII Text")

    parser.add_argument("--input", type=str, default="data/ascii_images/input.jpg", help="Input image path")
    parser.add_argument("--output", type=str, default="data/ascii_images/image_text.txt", help="Output text file path")
    parser.add_argument("--mode", type=str, default="standard", choices=["standard", "complex"], help="Type of character list")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    user_choice = get_args()
    get_data(user_choice)
    main()
