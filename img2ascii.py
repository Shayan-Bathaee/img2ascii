# This file takes an image as input and converts it into ascii text
# Creation Date: June 30th 2021
# creator: Shayan Bathaee
# step 1: Process the image
# step 2: convert it to grayscale
# step 3: resize image
# step 4: assign each pixel in the image a grayscale value
# step 5: print the image in ascii based on the greyscale value

from PIL import Image, ImageOps
import numpy as np
import sys

def img2ascii(img, width, outputFileName, inverted):
    # choose the horizontal dimension of the image
    w, h = img.size 
    if width > w:
        print(f"FAILED: Choose a size smaller than or equal to {w}")
        return False
    asciiWidth = width
    ratio = asciiWidth / w
    asciiHeight = int(ratio * (h/2))
    img = img.resize((asciiWidth, asciiHeight))                 # resize the image to the ascii dimensions
    img = ImageOps.grayscale(img)

    scale = " .:-=+*#%@"
    main_print = []

    for i in range(asciiHeight):
        for j in range(asciiWidth):
            color = img.getpixel((j, i))                        # get color
            color = int(color / 25.6)                           # scale it to our characters
            if inverted:
                main_print.append(scale[int(color)])            # index from the front    
            else:
                main_print.append(scale[-int(color + 1)])       # index from the back
            if j == (asciiWidth - 1):
                main_print.append('\n')

    if outputFileName == "":                                    # if no output file was given, just print to console
        print(''.join(main_print))
    else:
        outputFile = open(outputFileName, 'w')
        outputFile.write(''.join(main_print))


width = 100           # set default parameters
outputFileName = ""
inverted = False


if '-w' in sys.argv:
    width = int(sys.argv[sys.argv.index('-w') + 1])
if '-o' in sys.argv:
    outputFileName = sys.argv[sys.argv.index('-o') + 1]
if '-i' in sys.argv:
    if sys.argv[sys.argv.index('-i') + 1] == 'inverted':
        inverted = True

if '-usage' in sys.argv:
    print("\tUSAGE: python img2ascii.py <image-file> -w <ascii-width> -i <inverted/non-inverted> -o <output-file>")
    print("\tSee https://github.com/Shayan-Bathaee/img2ascii for more information")
else:
    img = Image.open(sys.argv[1]) # get the name of the image
    img2ascii(img, width, outputFileName, inverted)
