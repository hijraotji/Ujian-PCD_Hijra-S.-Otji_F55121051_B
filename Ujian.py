import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# fungsi untuk menampilkan gambar di tengah
def center_image():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    x = (canvas_width - img_tk.width()) / 2
    y = (canvas_height - img_tk.height()) / 2
    canvas.create_image(x, y, anchor='nw', image=img_tk)

# fungsi untuk memasukkan gambar
def load_image():
    global img_original, img_tk
    filename = filedialog.askopenfilename()
    img_original = Image.open(filename)
    img_tk = ImageTk.PhotoImage(img_original)
    canvas.delete("all") # hapus semua gambar yang sudah ditampilkan sebelumnya
    center_image() # menampilkan gambar di tengah

# fungsi untuk memperbaiki kontras
def adjust_contrast():
    global img_original, img_tk
    img_new = img_original.point(lambda x: x*1.5)
    img_tk = ImageTk.PhotoImage(img_new)
    canvas.delete("all") # hapus semua gambar yang sudah ditampilkan sebelumnya
    center_image() # menampilkan gambar di tengah

# fungsi untuk memperbaiki kecerahan
def adjust_brightness():
    global img_original, img_tk
    img_new = img_original.point(lambda x: x*0.5)
    img_tk = ImageTk.PhotoImage(img_new)
    canvas.delete("all") # hapus semua gambar yang sudah ditampilkan sebelumnya
    center_image() # menampilkan gambar di tengah

# fungsi untuk menampilkan semua gambar
def show_all():
    global img_original, img_tk
    img_contrast = img_original.point(lambda x: x*1.5)
    img_brightness = img_original.point(lambda x: x*0.5)
    img_all = Image.new("RGB", (img_original.width*3, img_original.height))
    img_all.paste(img_original, (0, 0))
    img_all.paste(img_contrast, (img_original.width, 0))
    img_all.paste(img_brightness, (img_original.width*2, 0))
    img_tk = ImageTk.PhotoImage(img_all)
    canvas.delete("all")  # hapus semua gambar yang sudah ditampilkan sebelumnya
    canvas.create_image(0, 0, anchor='nw', image=img_tk)
    canvas.image = img_tk

# membuat GUI
root = tk.Tk()
root.title("Aplikasi Penerapan Perbaikan Citra")

# membuat tombol untuk memasukkan gambar
load_button = tk.Button(root, text="Masukkan Gambar", command=load_image)
load_button.grid(row=0, column=0, padx=10, pady=10)

# membuat tombol untuk memperbaiki kontras
contrast_button = tk.Button(root, text="Perbaiki Kontras", command=adjust_contrast)
contrast_button.grid(row=0, column=1, padx=10, pady=10)

# membuat tombol untuk memperbaiki kecerahan
brightness_button = tk.Button(root, text="Perbaiki Kecerahan", command=adjust_brightness)
brightness_button.grid(row=0, column=2, padx=10, pady=10)

# membuat kotak untuk menampilkan gambar
canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# membuat tombol untuk menampilkan semua gambar
show_all_button = tk.Button(root, text="Tampilkan Semua", command=show_all)
show_all_button.grid(row=0, column=3, padx=10, pady=10)

# membuat label untuk menampilkan informasi pembuat program
creator_label = tk.Label(root, text="Nama : HIJRA S. OTJI, NIM : F55121051, Kelas : B]")
creator_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# menjalankan GUI
root.mainloop()

