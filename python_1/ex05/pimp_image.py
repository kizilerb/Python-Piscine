import numpy as np
import PIL.Image as img

def ft_invert(array):
    inverted = 255 - array.copy()
    img.fromarray(inverted).show()
    return (inverted)


def ft_red(array): #RGB
    red_img = array.copy()
    red_img[:, :, 1] *= 0
    red_img[:, :, 2] *= 0
    img.fromarray(red_img).show()
    return (red_img)
    

def ft_green(array):
    green_img = array.copy()
    green_img[:, :, 0] -= green_img[:, :, 0]
    green_img[:, :, 2] -= green_img[:, :, 2]
    img.fromarray(green_img).show()
    return (green_img)


def ft_blue(array):
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    img.fromarray(blue_img).show()
    return (blue_img)


def ft_grey(array):
#your code here
