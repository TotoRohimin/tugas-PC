import cv2
import numpy as np

def translasi(image, tx, ty):
    # Membuat matriks translasi
    matriks_translasi = np.float32([[1, 0, tx], [0, 1, ty]])

    # Melakukan translasi menggunakan warpAffine
    hasil_translasi = cv2.warpAffine(image, matriks_translasi, (image.shape[1], image.shape[0]))

    return hasil_translasi

def rotasi(image, sudut_rotasi):
    # Mendapatkan tengah citra
    titik_tengah = (image.shape[1] // 2, image.shape[0] // 2)

    # Membuat matriks rotasi
    matriks_rotasi = cv2.getRotationMatrix2D(titik_tengah, sudut_rotasi, 1.0)

    # Melakukan rotasi menggunakan warpAffine
    hasil_rotasi = cv2.warpAffine(image, matriks_rotasi, (image.shape[1], image.shape[0]))

    return hasil_rotasi

def skalasi(image, skala_x, skala_y):
    # Membuat matriks skalasi
    matriks_skalasi = np.float32([[skala_x, 0, 0], [0, skala_y, 0]])

    # Melakukan skalasi menggunakan warpAffine
    hasil_skalasi = cv2.warpAffine(image, matriks_skalasi, (image.shape[1], image.shape[0]))

    return hasil_skalasi

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

    # Panggil fungsi-fungsi geometri
    image_translasi = translasi(image, 50, 30)
    image_rotasi = rotasi(image, 45)
    image_skalasi = skalasi(image, 1.5, 1.5)

    # Tampilkan gambar hasil operasi geometri
    cv2.imshow('Hasil Translasi', image_translasi)
    cv2.imshow('Hasil Rotasi', image_rotasi)
    cv2.imshow('Hasil Skalasi', image_skalasi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
