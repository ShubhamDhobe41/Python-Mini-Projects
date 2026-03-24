from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slider View")

# list of image path
image_path = [
    r"D:\Python projects\Image_slider\Image\image1.jpg",
    r"D:\Python projects\Image_slider\Image\image2.jpg",
    r"D:\Python projects\Image_slider\Image\image3.jpg",
    r"D:\Python projects\Image_slider\Image\image4.jpg",
    r"D:\Python projects\Image_slider\Image\image5.jpg"
]

# Resize images
image_size = (800, 600)
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(img) for img in images]

# Create label
label = tk.Label(root)
label.pack()

# Create cycle iterator
slideshow = cycle(photo_images)

def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo   # keep reference

    root.after(3000, update_image)  # change every 3 sec

def start_sliding():
    update_image()

play_btn = tk.Button(root, text='Play Slide', command=start_sliding)
play_btn.pack()

root.mainloop()