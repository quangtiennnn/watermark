import os
from PIL import Image,ImageOps
"""Import IMG"""
path_logo = "logo"
path_undone = "undone"
path_done = "done"
logo = Image.open(os.path.join(path_logo,'logo.png'))

"""Convert to PNG"""
def convert_png(im):
    return im.save(os.path.join(path_undone,file_list[0]+".png"))
for filename in os.listdir(path_undone):
    file_list = filename.split(".")
    if (file_list[1] != "png"):
        im = Image.open(os.path.join(path_undone,filename))
        # Transpose with respect to EXIF data
        im = ImageOps.exif_transpose(im)
        convert_png(im)
        os.remove(os.path.join(path_undone,filename))

"""Adding Logo"""
# LOGO SIZE
choose = int(input("[1]: Top Left\n[2]: Top Right\n[3]: Bot Left\n[4]: Bot Right\nChoose:  "))
def logo_configure(im):
    times = ((1/5) * im.width) / logo.width
    width = int(logo.width * times)
    height = int(logo.height * times)
    return logo.resize((width, height))
def logo_import(im,logo):
    padding = int((1 / 5) * logo.width)
    area = corners[choose]
    im.paste(logo, area, mask = logo)
    return im
def choose_conners(im,logo):
    padding = int((1 / 5) * logo.height)
    corners = {
        1: (0 + padding, 0 + padding),
        2: (im.width - logo.width - padding, 0 + padding),
        3: (0 + padding, im.height - logo.height - padding),
        4: (im.width - logo.width - padding, im.height - logo.height - padding),
    }
    return corners

"""Multi Files"""
for filename in os.listdir(path_undone):
    im = Image.open(os.path.join(path_undone,filename))
    new_logo = logo_configure(im)
    corners = choose_conners(im,new_logo)
    new_im = logo_import(im,new_logo)
    new_im.save(os.path.join(path_done,filename))
    os.remove(os.path.join(path_undone,filename))

