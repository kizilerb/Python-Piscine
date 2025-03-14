import PIL.Image as img
import numpy as np
import os

def ft_load(path: str) -> np.array:
    try:
        if path.lower().endswith(".jpg", ".jpeg"):
            raise AssertionError("Only JPG and JPEG file formats are handled")
        elif not os.path.exists(path) or not os.path.isfile(path):
            raise AssertionError("Please use a valid file path")
        image = img.open(path)
        img_rgb = image.convert("RGB")
        print(f"The shape of image is: {image.format}")
        return (np.array(img.size(img_rgb)))
    except AssertionError as e:
        print("Error:", e)
        return(np.array(0))

