from PIL import Image, ImageDraw, ImageFont

def overlay_translated_text(image_path, text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFonte.load_default()
    x, y = 10, 10

    for line in text.split('\n'):
        draw.text((x, y), line, fill='black', font=font)
        y += 15

    image.save(output_path)