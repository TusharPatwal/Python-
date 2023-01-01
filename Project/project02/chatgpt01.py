from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, font_size=24):
    # create an image
    image = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # select a font
    font = ImageFont.truetype('arial.ttf', font_size)

    # draw the text on the image
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    # save the image
    image.save('handwriting.png')

text_to_handwriting('hrdsktygr trh fgdvrtyb btyft r6bvtr byjtvyrtc ntubyrt nbyrthverc ybrtc')
