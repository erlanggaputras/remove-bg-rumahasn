from PIL import Image
from rembg import remove
import os

# === INPUT & OUTPUT CONFIG ===
input_path = "C:/Users/Erlangga/Downloads/pasfoto2.jpg"   # Ganti dengan nama file gambar kamu
output_path = "output.png"  # Gunakan .png untuk transparansi, atau .jpg untuk background putih

# === REMOVE BACKGROUND ===
try:
    with Image.open(input_path) as img:
        img = img.convert("RGBA")  # Konversi ke RGBA agar rembg bisa memproses transparansi
        output = remove(img)

        # Jika output file ingin disimpan sebagai JPG (yang tidak mendukung transparansi)
        if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
            # Konversi transparansi menjadi background putih
            background = Image.new("RGB", output.size, (255, 255, 255))
            background.paste(output, mask=output.split()[3])  
            background.save(output_path, format="JPEG")
        else:
            output.save(output_path, format="PNG")

        print(f"Sukses! File disimpan sebagai: {output_path}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
