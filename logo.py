import os
from PIL import Image

def add_logo_to_images(image_folder, logo_path, output_folder, logo_scale=0.1):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the logo image
    logo = Image.open(logo_path)
    
    # Process each image in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)

            # Get image size and calculate new logo size (as a percentage of the image size)
            image_width, image_height = image.size
            new_logo_width = int(image_width * logo_scale)
            new_logo_height = int(logo.size[1] * (new_logo_width / logo.size[0]))  # Keep the aspect ratio
            
            # Resize the logo
            resized_logo = logo.resize((new_logo_width, new_logo_height), Image.LANCZOS)

            # Calculate the bottom-right position for the logo
            position = (image_width - new_logo_width, image_height - new_logo_height)

            # Paste the resized logo on the image (with transparency handling for PNGs)
            image.paste(resized_logo, position, resized_logo if resized_logo.mode == 'RGBA' else None)

            # Save the modified image to the output folder
            output_path = os.path.join(output_folder, filename)
            image.save(output_path)

            print(f"Logo added to {filename} and saved to {output_path}")

image_folder = '/home/edward/Desktop/Nails'
logo_path = '/home/edward/Desktop/logo2.png'
output_folder = '/home/edward/Desktop/images-l'

"""
Adjust logo scale. 
0.1 = 10% of image width
"""
add_logo_to_images(image_folder, logo_path, output_folder, logo_scale=0.25)
