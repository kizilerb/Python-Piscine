from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as img

#croplanmaması gerekiyor gibi geldi subjectte size aynı kalmış, kare fotoğraf bul
def cropping(image, h, w):
    cropped = image.crop(((w//2)-250, (h//2)-250, (w//2)+250, (h//2)+250))
    transposed = np.transpose(cropped)
    img_array = np.array(transposed)
    print(f"New shape after slicing: {img_array.shape}")
    print(img_array)
    # plotting and visual output 
    plt.imshow(img_array, cmap="gray")
    plt.xlabel("X-axis (pixels)")
    plt.ylabel("Y-axis (pixels)")
    plt.title("Zoomed Image")
    plt.show()
    return (img_array)

def main():
    image = ft_load("./animal.jpeg")
    print(image)
    # converting image from array to image and in a grayscale format
    img2rotate = img.fromarray(image)
    img2rotate = img2rotate.convert("L")
    # getting grayscaled image and also original pixel size of the photo to crop
    cropping(img2rotate, len(image), len(image[0]))

if __name__ == "__main__":
    main()