from load_image import ft_load
import PIL.Image as img
import numpy as np
import matplotlib.pyplot as plt 


def zooming(image, h, w):
    # cropping a small region to resize it and give zoomed effect, (left, top, right, bottom)
    cropped = image.crop(((w//2)-150, (h//2)-150, (w//2)+150, (h//2)+150)) 
    zoomed = cropped.resize((400,400))
    # zoomed.show()
    img_array = np.array(zoomed)
    imgplot = plt.imshow(img_array, cmap="gray")
    plt.xlabel("X-axis (pixels)")
    plt.ylabel("Y-axis (pixels)")
    plt.title("Zoomed Image")
    plt.show()


def main():
    image = ft_load("./animal.jpg")
    print(image)
    # converting image from array to image and in a grayscale format
    img2zoom = img.fromarray(image).convert("L")
    # getting grayscaled image and also original pixel size of the photo to slice
    zooming(img2zoom, len(image), len(image[0]))


if __name__ == "__main__":
    main()