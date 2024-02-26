import cv2
import numpy as np

def main():
    # Baca gambar
    image = cv2.imread('python/captured_image.jpg')

    if image is None:
        print("Gambar tidak ditemukan. Pastikan path gambar benar.")
        return

    # Tampilkan gambar asli
    cv2.imshow('Gambar Asli', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Contoh operasi aritmatika (menambahkan nilai ke saluran biru)
    blue_channel = image[:, :, 0]
    added_value = 50
    blue_channel = cv2.add(blue_channel, added_value)

    # Gabungkan kembali saluran biru dengan saluran hijau dan merah
    image[:, :, 0] = blue_channel

    # Tampilkan gambar hasil operasi aritmatika
    cv2.imshow('Hasil Operasi Aritmatika', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

    # nyoba1
