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

    # Making background black or white; default="white"
    if user_choice.background == "white":
        bg_code = (255, 255, 255)
        bg = "white"
    else:
        bg_code = (0, 0, 0)
        bg = "black"

    input= user_choice.input # Default video ="data/ascii_images/input.jpg"
    output = user_choice.output # Default video ="data/ascii_images/coloured_image.jpg"

    return  font, char_list, num_chars, num_cols, bg_code, bg, input, output

def main():

    # Getting data from get_data function
    font, char_list, num_chars, num_cols, bg_code, bg, input, output = get_data(user_choice)

    # Reading Input Image
    image = cv2.imread(input, cv2.IMREAD_COLOR)

    # Converting Color Image to Grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Extracting dimesions from Image
    height, width, z = image.shape

    # Defining height and width of each cell==pixel
    cell_width = width / num_cols
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    
    # Calculating Height and Width of the output Image
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = 2 * char_height * num_rows

    # Making a new Image using PIL; mode="RGB"; RGB-(3x8-bit pixels, true color)
    out_image = Image.new("RGB", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)

   # Mapping the Characters
    for i in range(num_rows):
        for j in range(num_cols):
            min_height = min(int((i + 1) * cell_height), height)
            row_pix = int(i * cell_height)

            partial_image = image[row_pix:min_height,
                            int(j * cell_width):min(int((j + 1) * cell_width), width), :]
            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_height * cell_width)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
            char = char_list[min(int(np.mean(partial_image) * num_chars / 255), num_chars - 1)]

            # Draw string at a given position (x,y) 
            draw.text((j * char_width, i * char_height), char, fill=partial_avg_color, font=font)

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

    parser = argparse.ArgumentParser("ASCII Coloured Image")

    parser.add_argument("--input", type=str, default="data/ascii_images/input.jpg", help="Input image path")
    parser.add_argument("--output", type=str, default="data/ascii_images/coloured_image.jpg", help="Output image path")
    parser.add_argument("--mode", type=str, default="standard", choices=["standard", "complex"], help="Type of character list")
    parser.add_argument("--background", type=str, default="white", choices=["black", "white"], help="Background's colour")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    user_choice = get_args()
    get_data(user_choice)
    main()
