from PIL import Image, ImageDraw, ImageFont

def add_caption(image_path, caption, output_path, font_path='arial.ttf', font_size=20, text_color=(0, 0, 0)):
    """
    Add a caption to an existing image.

    Args:
        image_path (str): The path to the input image.
        caption (str): The text to add as a caption.
        output_path (str): The path to save the output image.
        font_path (str): The path to the TTF font file to use. Default is 'arial.ttf'.
        font_size (int): The size of the font. Default is 20.
        text_color (tuple): The color of the text in RGB format. Default is black (0, 0, 0).
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(caption, font)
    image_width, image_height = image.size
    x_position = (image_width - text_width) // 2
    y_position = image_height - text_height - 10

    draw.text((x_position, y_position), caption, font=font, fill=text_color)
    image.save(output_path)

# Example usage
add_caption('input_image.jpg', 'Example Caption', 'output_image.jpg')
