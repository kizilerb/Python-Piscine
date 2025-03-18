import numpy as np
import PIL.Image as img


def ft_invert(array):
    inverted = array.copy()
    inverted = 255 - inverted
    img.fromarray(inverted).show()
    return (inverted)


def ft_red(array):
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
    grey_img = array.copy()
    ratio = np.array([1/3, 1/3, 1/3])
    grey_values = np.dot(array[:, :, :3], ratio)
    grey_img[:, :, 0] = grey_values
    grey_img[:, :, 1] = grey_values
    grey_img[:, :, 2] = grey_values
    img.fromarray(grey_img).show()
    return (grey_img)
