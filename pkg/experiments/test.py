from PIL import Image
import numpy
import cv2

# Front Image
filename = 'mouth.png'

# Back Image
filename1 = 'back.png'

# Open Front Image
frontImage = Image.open(filename)

# Open Background Image
background = Image.open(filename1)

# Convert image to RGBA
frontImage = frontImage.convert("RGBA")

# Convert image to RGBA
background = background.convert("RGBA")

# Calculate width to be at the center
width = (background.width - frontImage.width) // 2

# Calculate height to be at the center
height = (background.height - frontImage.height) // 2

# Paste the frontImage at (width, height)
background.paste(frontImage, (width+50, height+100), frontImage)

# Save this image
background.save("new.png", format="png")