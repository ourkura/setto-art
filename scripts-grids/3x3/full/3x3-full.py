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

# Iterate over the 9 block sections
for row in range(3):
    for col in range(3):
        # Determine the x and y coordinates of the top left corner of the block
        x = col * 200
        y = row * 200

        # Choose a random file from the list
        filename = random.choice(png_files)

        # Construct the full file path
        filepath = os.path.join(png_dir, filename)

        # Open the PNG file
        bitmap = Image.open(filepath)

        # Resize the image to fit the block
        bitmap = bitmap.resize((200, 200))

        # Paste the resized image onto the main image
        image.paste(bitmap, (x, y))

# Save the image in PNG format
image.save("image.png", "PNG")
