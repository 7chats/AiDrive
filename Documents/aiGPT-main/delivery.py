from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

def generate_delivery_image():
    # Create a new image with a white background
    width, height = 800, 600
    image = Image.new('RGB', (width, height), color='white')
    
    # Load the AiDrive logo
    logo = Image.open('aidrive_logo.png')
    
    # Resize the logo and paste it onto the image
    logo_size = (200, 200)
    logo = logo.resize(logo_size)
    image.paste(logo, (50, 50))
    
    # Draw a rectangle to represent the package
    package_size = (300, 300)
    package_pos = (width // 2 - package_size[0] // 2, height // 2 - package_size[1] // 2)
    package_rect = package_pos + tuple(map(sum, zip(package_pos, package_size)))
    draw = ImageDraw.Draw(image)
    draw.rectangle(package_rect, outline='black', width=5)
    
    # Add the label "AiDrive Delivery Service" to the package
    font = ImageFont.truetype('arial.ttf', size=36)
    label_text = "AiDrive Delivery Service"
    label_size = draw.textsize(label_text, font=font)
    label_pos = (package_pos[0] + package_size[0] // 2 - label_size[0] // 2, package_rect[3] + 20)
    draw.text(label_pos, label_text, fill='black', font=font)
    
    # Return the image
    return image


def add_text_to_image(image, text):
    # Add text to the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=36)
    text_size = draw.textsize(text, font=font)
    text_pos = (image.width // 2 - text_size[0] // 2, image.height // 2 - text_size[1] // 2)
    draw.text(text_pos, text, fill='black', font=font)
    return image


def label_package(image):
    # Draw a label on the package
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=48)
    label_text = "Fragile"
    label_size = draw.textsize(label_text, font=font)
    label_pos = (image.width - label_size[0] - 20, 20)
    draw.text(label_pos, label_text, fill='red', font=font)
    return image


def package_delivery_image(width=600, height=400):
    # Create a blank canvas of the specified size
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Draw a delivery truck on the left side of the image
    truck_width = int(width * 0.3)
    truck_height = int(height * 0.6)
    truck_left = int(width * 0.05)
    truck_top = int(height * 0.2)
    truck_right = truck_left + truck_width
    truck_bottom = truck_top + truck_height
    img[truck_top:truck_bottom, truck_left:truck_right, :] = [255, 0, 0]  # red truck
    
    # Draw a package on the right side of the image
    package_width = int(width * 0.2)
    package_height = int(height * 0.3)
