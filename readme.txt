- Setting up:

First, make sure you have Python installed on your computer.
Open a command prompt or terminal.
Install Pillow by typing: pip install Pillow


- Create a new Python file and Copy the source code provided into this file.


- Understanding the code:

-- These lines import the necessary modules. PIL is the Pillow library for image processing, and os is for file operations.
pythonCopyfrom PIL import Image
import os

-- This defines a function that takes three parameters: the path to the input image, where to save the output, and the quality level.
pythonCopydef compress_image(input_path, output_path, quality):

-- This opens the image file.
pythonCopywith Image.open(input_path) as img:

-- This converts RGBA images (with transparency) to RGB, as JPEG doesn't support transparency.
pythonCopyif img.mode == 'RGBA':
    img = img.convert('RGB')

-- This saves the image as a JPEG with the specified quality.
pythonCopyimg.save(output_path, 'JPEG', quality=quality)

--The rest of the function calculates and prints the file size reduction.

--At the bottom of the file, you'll see:
pythonCopyinput_image = 'path/to/your/input/image.png'
output_image = 'path/to/your/output/image.jpg'
quality = 85
Replace 'path/to/your/input/image.png' with the actual path to your image file.
Replace 'path/to/your/output/image.jpg' with where you want to save the compressed image.
Adjust the quality value if desired (0-95, lower means more compression).

- Running the script:

Open a command prompt or terminal.
Navigate to the directory containing your Python file.
Run the script by typing: python [your file name]


- Check the results:

Look for the output image in the specified location.


//////////////////////////////////////////////////////////////////// UPDATE:
an updated version of the script that handles both JPEG and PNG compression:

Key changes in this version:

We detect the output file format based on the file extension.
For PNG files, we use optimize=True to enable ZLIB compression optimization.
For PNG, the quality parameter is used as the compress_level (0-9), where higher values mean more compression (opposite of JPEG).
The script now handles both JPEG and PNG formats automatically based on the output file extension.

To use this for PNG to PNG compression:

Set your input_image path to your PNG file.
Set your output_image path with a .png extension.
Adjust the quality value. For PNG, this should be between 0-9, where 9 is the highest compression level.

Remember that PNG uses lossless compression, so the visual quality won't change, but higher compression levels may take longer to process.