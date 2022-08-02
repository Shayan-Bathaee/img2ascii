# img2ascii
This python program allows the user to convert any image into ASCII art. The inputs to this program are an image file and option parameters. The output, presented either in the console or in a .txt file, is an ASCII string representing the image.

## Files
- **img2ascii.py:** This file contains the python program that converts images into ASCII text.
- **cow_example:** This folder contains an example image with two different output files. 
  - **cow.jpg:** This is the example image of a cow
  - **std_cow.txt:** This is the standard output. It was created using no width flag and no inverted flag. 
  - **inverted_cow_500.txt:** This output was created by setting the width flag to 500 and using the inverted flag. 

## Usage
To run img2ascii, open up a command prompt window and navigate to the location of the file. Next, run the following command:

`python img2ascii.py <image-file> -w <ascii-width> -i <inverted/non-inverted> -o <output-file>`

There are a few different flags in this command. Here is what they mean:
- `-w` is the character width of the outputted ASCII text art.
  - For example, putting `-w 500` will result in ASCII art that is 500 characters wide.
  - If the width parameter is greater than the width of the image, an error will occur and the program will display the maximum width you can choose.
  - If no width parameter is provided, the default width will be 100 characters.
- `-i` tells the program to invert or not invert the image.
  - If your computer is in dark mode, putting `-i inverted` will make the picture look normal over the dark background.
  - If no invert parameter is provided, the default setting is non-inverted.
- `-o` is the name of the output file.
  - The output file should be a .txt file.
  - If the output file already exists, the contents will be overwritten.
  - If the output file doesn't exist, it will be created.
  - If no output file parameter is provided, the program will print the output to the console. 
The order of these flags does not matter.
 
 ## Implementation
 A high-level description of the logical flow of this program is as follows:
 1. Take in the image from user input.
 2. Greyscale the image (make the image black and white).
 3. Resize the image to match the final dimensions of the ASCII art.
 4. For every pixel in the image, get the color code of that pixel.
 5. Scale that value down so it can be used to index the character set (` .:-=+*#%@`).
 
Some other important attributes to the program:
- The height of the ASCII text art is determined using the following process:
  1. Get the ratio of the ASCII text art width to the original image width.
  2. Multiply the original image height by the ratio.
  3. Divide by two (ASCII characters are twice as tall as they are wide).
- Because the image is greyscaled, the method `getpixel()` only returns one color value instead of a tuple of (R, G, B) values.
- There are 256 color values and 10 characters in the set, so dividing the color value by 25.6 and rounding it scales it down to the character set.
- The output is stored as an array and is converted into a string at the end using the `.join` method.

 
