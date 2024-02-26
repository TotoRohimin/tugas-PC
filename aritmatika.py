import cv2
import numpy as np

# Fungsi untuk menampilkan citra menggunakan OpenCV
def tampilkan_citra(judul, citra):
    cv2.imshow(judul, citra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Baca citra
citra_path = 'captured_image.jpg'
citra = cv2.imread(citra_path)

# Pastikan citra berhasil dibaca
if citra is None:
    print(f'Gagal membaca citra di path: {citra_path}')
    exit()

# Tampilkan citra asli
tampilkan_citra('Citra Asli', citra)

# Operasi aritmatika: Penambahan
konstanta_penambahan = 50
citra_penambahan = cv2.add(citra, konstanta_penambahan)

# Tampilkan citra setelah penambahan
tampilkan_citra('Citra Setelah Penambahan', citra_penambahan)

# Operasi aritmatika: Pengurangan
konstanta_pengurangan = 50
citra_pengurangan = cv2.subtract(citra, konstanta_pengurangan)

# Tampilkan citra setelah pengurangan
tampilkan_citra('Citra Setelah Pengurangan', citra_pengurangan)

# Operasi aritmatika: Perkalian
faktor_perkalian = 1.5
citra_perkalian = cv2.multiply(citra, faktor_perkalian)

# Tampilkan citra setelah perkalian
tampilkan_citra('Citra Setelah Perkalian', citra_perkalian)

# Operasi aritmatika: Pembagian
faktor_pembagian = 2
citra_pembagian = cv2.divide(citra, faktor_pembagian)

# Tampilkan citra setelah pembagian
tampilkan_citra('Citra Setelah Pembagian', citra_pembagian)
