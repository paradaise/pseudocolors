import tkinter as tk
from tkinter import filedialog
import matplotlib.image as mpimg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def apply_pseudocolor():
    image_path = filedialog.askopenfilename()
    img = mpimg.imread(image_path)

    # Преобразование изображения в градации серого
    gray_img = 0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]

    # Нормализация изображения в градациях серого
    gray_img = gray_img / np.max(gray_img)

    # Создание палитры псевдоколоирования
    pseudo_palette = np.zeros((256, 3))
    pseudo_palette[:, 0] = np.sin(np.linspace(0, 2 * np.pi, 256))  # Красный канал
    pseudo_palette[:, 1] = np.cos(np.linspace(0, 2 * np.pi, 256))  # Зеленый канал
    pseudo_palette[:, 2] = np.sin(np.linspace(0, np.pi, 256))  # Синий канал

    # Применение псевдоколоирования
    pseudo_img = pseudo_palette[(gray_img * 255).astype(int)]

    fig = Figure(figsize=(25, 25))
    axs = fig.subplots(1, 3)
    axs[0].imshow(img)
    axs[0].set_title("Original Image")
    axs[1].imshow(gray_img, cmap="gray")
    axs[1].set_title("Grayscale Image")
    axs[2].imshow(pseudo_img)
    axs[2].set_title("Pseudocolored Image")

    for widget in root.winfo_children():
        widget.destroy()

    button = tk.Button(
        root, text="Выберите другое изображение", command=apply_pseudocolor
    )
    button.pack()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = tk.Tk()
root.title("Псевдоцвета by Viktor")
root.geometry("1920x1080")
button = tk.Button(root, text="Выберите изображение", command=apply_pseudocolor)
button.pack()
root.mainloop()
