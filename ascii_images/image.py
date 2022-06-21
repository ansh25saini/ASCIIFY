# Dependencies
import cv2
import numpy as np
import argparse
from PIL import Image, ImageFont, ImageDraw, ImageOps

Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

# Getting initialized data 
def get_data(user_choice):

    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size= int(10 * 2)) # Scale = 2; Scale= Upsize output
    char_list= Character[user_choice.mode] # Character List; Default Mode = "standard"
    num_chars = len(char_list) # length of character list
    num_cols = 300 # Number of character for output's width
    
    # Making Background Black or White; Default="White"
    if user_choice.background == "white":
        bg_code = 255
        bg = "white"
    else:
        bg_code = 0
        bg = "black"
        
    input= user_choice.input # Default image ="data/ascii_images/input.jpg"
    output = user_choice.output # Default image ="data/ascii_images/image.jpg"

    return  font, char_list, num_chars, num_cols, bg_code, bg, input, output

def main():

    # Getting data from get_data function
    font, char_list, num_chars, num_cols, bg_code, bg, input, output = get_data(user_choice)
    
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

    # Calculating Height and Width of the output Image
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = 2 * char_height * num_rows

    # Making a new Image using PIL
    out_image = Image.new("L", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)

    # Mapping the Characters
    for i in range(num_rows):
        min_height = min(int((i + 1) * cell_height), height)
        row_pix = int(i * cell_height)
    
        # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
        # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
        line = "".join([char_list[min(int(np.mean(image[row_pix:min_height,
                                                  int(j * cell_width):min(int((j + 1) * cell_width),
                                                                          width)]) / 255 * num_chars), num_chars - 1)]                                                                          
                        for j in range(num_cols)]) + "\n"

        # Draw string at a given position (x,y)                
        draw.text((0, i * char_height), line, fill=255 - bg_code, font=font)
    
    # Inverting Image and removing excess borders
    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    else:
        cropped_image = out_image.getbbox()

    # Saving the new Image
    out_image = out_image.crop(cropped_image)
    out_image.save(output)

# Utility function for parsing arguments
def get_args():

    parser = argparse.ArgumentParser("ASCII Image")

    parser.add_argument("--input", type=str, default="data/ascii_images/input.jpg", help= "Input image path")
    parser.add_argument("--output", type=str, default="data/ascii_images/image.jpg", help="Output image path")
    parser.add_argument("--mode", type=str, default="standard", choices=["standard", "complex"], help="Type of character list")
    parser.add_argument("--background", type=str, default="white", choices=["black", "white"], help="Background's colour")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    user_choice = get_args()
    get_data(user_choice)
    main()
