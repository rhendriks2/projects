# https://www.youtube.com/watch?v=x6fHhNvcGjg

from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

# TK interface
root = Tk()
# As soon as program starts we want to close the window
root.withdraw()


# get image from user
filename = filedialog.askopenfilename(title="Select an Image")


def add_watermark(image, wm_text):
    # to create the image object and get the image width and height:
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    # font specifications
    font_size = int(image_width / 12)
    font = ImageFont.truetype('arial.ttf', size=font_size)  # make sure the font is available on your computer

    # coordinates to place watermark (you can specify them to your liking)
    x, y = int(image_width / 2), int(image_height / 2)

    # add the watermark
    draw.text(xy=(x, y), text=wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor="ms")

    # show the new image
    opened_image.save('new-and-watermarked.png')
    opened_image.show()


watermark_text = input("What is the watermark text? ")
add_watermark(filename, watermark_text)
