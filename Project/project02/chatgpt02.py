from PIL import Image, ImageDraw, ImageFont, ImageFilter

def text_to_sketch(text, font_size=24):
    # create an image
    image = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # select a font
    font = ImageFont.truetype('arial.ttf', font_size)

    # draw the text on the image
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    # convert the image to grayscale
    image = image.convert('L')

    # apply the sketch filter
    image = image.filter(ImageFilter.CONTOUR)

    # save the image
    image.save('sketch.png')

text_to_sketch('Hello, World!, i am tushar patwal')
