import PIL.Image as img
import numpy as np
import os


def ft_load(path: str) -> np.array:
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError(f"Only JPG and JPEG file formats are handled: {path} is not valid")
        elif not os.path.exists(path) or not os.path.isfile(path):
            raise AssertionError("Please use a valid file path")
        image = img.open(path)
        img_rgb = image.convert("RGB")
        img_array = np.array(img_rgb)
        print(f"The shape of image is: {img_array.shape}")
        return (img_array)
    except AssertionError as e:
        print("Error:", e)
        return (np.array(0))
