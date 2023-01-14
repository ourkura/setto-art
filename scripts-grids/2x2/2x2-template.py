import os
import random
from PIL import Image, ImageDraw, ImageFont

# Set the size of the image
width, height = 600, 600

# Set the directory containing the PNG files
png_dir = "png"

# Get a list of all the files in the directory
files = os.listdir(png_dir)

# Create a list of PNG files
png_files = []

# Iterate over the files in the directory
for file in files:
    # Check if the file name is not '.DS_Store'
    if file != ".DS_Store":
        # Add the file to the list of PNG files
        png_files.append(file)

# Create a blank image with a transparent background
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

# Iterate over the 4 block sections
for row in range(2):
    for col in range(2):
        # Determine the x and y coordinates of the top left corner of the block
        x = col * 300
        y = row * 300

        # Randomly choose whether to fill the block or not
        if random.choice([True, False]):
            # Choose a random file from the list
            filename = random.choice(png_files)

            # Construct the full file path
            filepath = os.path.join(png_dir, filename)

            # Open the PNG file
            bitmap = Image.open(filepath)

            # Resize the image to fit the block
            bitmap = bitmap.resize((300, 300))

            # Paste the resized image onto the main image
            image.paste(bitmap, (x, y))

# Save the image in PNG format
image.save("image.png", "PNG")