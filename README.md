# ASCIIFY : ASCII Art Generator

### This project is made as a part of the IITR ACM- Open Summer Project, 2022. It can be used to convert images and videos to [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art).

<img src="https://user-images.githubusercontent.com/103529456/174550041-724aba84-4df6-42e1-818e-20c831d37494.gif" alt="welcome_gif" width="1432"/>

## 📌 Table of Contents
* [Description / Internal Working](#description)
* [Features](#features)
* [Tech Stack / Dependencies](#tech-stack)
* [Getting Started / Setup](#getting-started)
* [Additional Task](#add_task)
* [User Guide](#📖-user-guide)
* [Challenges Faced and Learnings](#💡-challenges-faced-and-learnings)
* [Resources](#resources)
* [Bug Reporting](#bug)
* [Feature Request](#feature-request)

<a id="description"></a>
## 📓  Description / Internal Working
This project aims at converting images ( .jpg / .png) and videos (.mp4 / .avi) to ASCII encoded strings that look same as the original input. 

ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers. Media files (images / videos) can also be represented in the same format using different characters.

To convert an image to ASCII art, opencv and python pillow library have been used in the project. The input image is stored as a matrix having values on the basis of color intensity of the corresponding pixels. The image matrix is converted to grayscale values and height and width of the input image is calculated. Using the dimensions of the image, number of characters in the width of the output image and scale factor, the number of characters in the height of the output image are calculated. Using this and dimensions of the font used, the dimensions of the output image are calculated and a new image is formed using pillow library. Finally the characters are mapped onto the image, and excessive borders are removed to get the final output.
The mapping of the characters are done on the basis of the average intensity of the cell (pixel) and inserting the character from the character list having similar intensity.

To convert a video to ASCII art, each frame is processed as an individual image (as described in the process above) and all the frames are then appended to produce the final output.

<a id="features"></a>
## 🚀 Features
- Convert an image to ASCII art in text format (.txt).
- Convert an image to ASCII art in image format (.jpg / .png).
- Image outputs can either be in grayscale or colour format. Seperate programs for both have been included in the project.
- Convert a video to ASCII art in coloured format (.avi / .mp4).
- Image and video outputs can either be in black background or white background (dependent on the user input).
- All the outputs (text / images / videos) can either be made using standard set of characters or complex list of characters.
- [Add more features](#feature-request)...

<a id="tech-stack"></a>
## 💻 Tech Stack / Dependencies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

***Python*** : The complete project is written in python programming language.

***OpenCV*** : OpenCV has been used for image pre-processing.

***Numpy*** : To work with matrices.

***Pillow*** : Python library for creating font object, making new images and editing them.

***Visual Studio Code*** : Editor used in the project

<a id="getting-started"></a>
## 📦 Getting Started/ Setup

1. Clone this repository.

```javascript
  git clone https://github.com/ansh25saini/ASCIIFY.git
```  

2. Make and activate the virtual environment *env*

```javascript
  python -m venv env
  env/Scripts/activate
```

3. Instal requirements.txt

```javascript
  pip install -r requirements.txt
```

4. Finally to run the file (suppose ***coloured_image.py***)-  "python file_path"

```javascript
  python ascii_images/coloured_image.py
```

5. In order to see user input commands, use -  "python file_path -h"

```javascript
  python ascii_images/coloured_image.py -h
```
6. In order to provide user input (like input/output file, mode of character list or type of background), use -  "python file_path -mode complex"

```javascript
  python ascii_images/coloured_image.py --mode complex --background black
```
<a id="add_task"></a>
## 🚀 Additional Task
Apart from converting images into ASCII format of text, grayscale or coloured images, this project also asciify videos into coloured format videos of .avi / .mp4 type.

A seperate ***ascii_videos/coloured_video.py*** file has been added into the project. To know about how videos are converted to ASCII art, refer to [description](#description) section of this readme file.

The output videos will be in coloured video format with either black or white background depending on the user input. The user can also put the choice for the type of character list: standard or complex.

The following are the results for the given input video (the results are orginally in video format but here they are converted to gifs for the sake of simplicity; the orginal videos are present in ***data/ascii_videos/*** directory of the project)

* Input video used in the project; here (in readme file) it is in .gif format-
<img width="705" alt="Input Video" src="https://user-images.githubusercontent.com/103529456/174478053-5a5c9906-971e-44a7-bdf4-174a6a3dbcd3.gif">

* Output Video- coloured_video_white_standard : white background with standard character list. 
<img width="705" alt="coloured_video_white_standard" src="https://user-images.githubusercontent.com/103529456/174478052-6f177b01-256b-497b-92e9-6a599b71785d.gif">

* Output Video- coloured_video_white_complex  : white background with complex character list. 
<img width="705" alt="coloured_video_white_complex" src="https://user-images.githubusercontent.com/103529456/174478048-2c2560a3-2adb-48f7-94a2-942257ce67d2.gif">

* Output Video- coloured_video_black_standard : black background with standard character list.
<img width="705" alt="coloured_video_black_standard" src="https://user-images.githubusercontent.com/103529456/174478047-9652c285-070f-4c5d-9dbe-15c8fc6f647c.gif">

* Output Video- coloured_video_black_complex  : black background with complex character list. 
<img width="705" alt="coloured_video_black_complex" src="https://user-images.githubusercontent.com/103529456/174478044-a2445f31-a4b8-4e75-b270-861dfa8d9347.gif">

<a id="user Guide"></a>
## 📖 User Guide

### 1.  Image to ASCII art in image format ( .jpg / .png)
Either standard or complex type of character list, black or white background, and grayscale or coloured format outputs can be made. 
All the outputs are shown below:

* Input image used in the project (in .jpg format)-
<img width="705" alt="Input" src="https://user-images.githubusercontent.com/103529456/174477201-5ff3065a-c151-4a62-ab25-dd466355c16c.jpg">

* Output Image: image_white_standard (in .jpg format)
<img width="705" alt="image_white_standard" src="https://user-images.githubusercontent.com/103529456/174477197-630fd9b1-cdfa-4c7a-bcc5-622607408596.jpg">

* Output Image: image_white_complex (in .jpg format)
<img width="705" alt="image_white_complex" src="https://user-images.githubusercontent.com/103529456/174477195-9694e9a8-a760-4f94-a8a4-e991fe967f63.jpg">

* Output Image: image_black_standard (in .jpg format)
<img width="705" alt="image_black_standard" src="https://user-images.githubusercontent.com/103529456/174477192-ab553034-381f-4ff8-bbe2-c71cc65e7b4a.jpg">

* Output Image: image_black_complex (in .jpg format)
<img width="705" alt="image_black_complex" src="https://user-images.githubusercontent.com/103529456/174477189-df763de0-d2dc-404d-9247-bcc4f1d42d5b.jpg">

* Output Image: coloured_image_white_standard (in .jpg format)
<img width="705" alt="coloured_image_white_standard" src="https://user-images.githubusercontent.com/103529456/174477186-20cb5a0a-2e6d-4b03-b426-ac518ab35176.jpg">

* Output Image: coloured_image_white_complex (in .jpg format)
<img width="705" alt="coloured_image_white_complex" src="https://user-images.githubusercontent.com/103529456/174477185-1b819254-0f4a-4759-8428-da4c27b5c206.jpg">

* Output Image: coloured_image_black_standard (in .jpg format)
<img width="705" alt="coloured_image_black_standard" src="https://user-images.githubusercontent.com/103529456/174477182-2a769975-d754-4147-8ef3-e3e6a0a7c0eb.jpg">

* Output Image: coloured_image_black_complex (in .jpg format)
<img width="705" alt="coloured_image_black_complex" src="https://user-images.githubusercontent.com/103529456/174477181-f50c7ce4-3bbc-4bb2-91d4-eb8f8857d53d.jpg">

### 2. Image to ASCII art in text format (.txt)
Either standard or complex type of character list can be used.
Output files are present in data/ascii_images folder of the project directory.

* Output file- [image_text_standard](https://github.com/ansh25saini/ASCIIFY/files/8935213/image_text_standard.txt)
* Output file- [image_text_complex](https://github.com/ansh25saini/asciify/files/8935182/image_text_complex.txt) 

### 3. Video to ASCII art in coloured format (.avi / .mp4)
Refer to [Additional Task](#add_task) section of this readme file.

<a id="challenges"></a>
## 💡 Challenges faced and learnings

- Got familiar with OpenCV and Pillow library for working with media files.
- Learnt about how digital images are stored in a computer.
- Faced a major challenge in mapping the characters onto the image.
- Learnt about how videos are processed frame-by-frame.

<a id="resources"></a>
## 📚 Resources

* [Help from IIT Roorkee ACM Student Chapter](https://iitr.acm.org/#/)
* [Wiki Article on ASCII Art and Images](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
* [How Digital Images are stored in a computer](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)
* [Handbook for OpenCV and Pillow](https://medium.com/analytics-vidhya/the-ultimate-handbook-for-opencv-pillow-72b7eff77cd7)

<a id="bug"></a>
## 🐛 Bug Reporting
Feel free to [open an issue](https://github.com/ansh25saini/ASCIIFY/issues) on GitHub if you find bugs.

<a id="feature-request"></a>
## ⭐ Feature Request
- Feel free to [open an issue](https://github.com/ansh25saini/ASCIIFY/issues) on GitHub to add any additional features you feel could enhance this project.  
- You can also discuss and provide suggestions to me on [LinkedIn](https://www.linkedin.com/in/ansh25saini/).

---------
  ```javascript
  if (youEnjoyed) {
      ⭐ starThisRepository();
  }
  ```
-----------