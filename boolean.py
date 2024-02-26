import cv2
import numpy as np

def operasi_boolean(citra1, citra2, jenis_operasi):
    # Terapkan operasi boolean pada dua citra
    if jenis_operasi == 'and':
        hasil_operasi = cv2.bitwise_and(citra1, citra2)
    elif jenis_operasi == 'or':
        hasil_operasi = cv2.bitwise_or(citra1, citra2)
    elif jenis_operasi == 'xor':
        hasil_operasi = cv2.bitwise_xor(citra1, citra2)
    elif jenis_operasi == 'not':
        hasil_operasi = cv2.bitwise_not(citra1)
    else:
        print("Jenis operasi boolean tidak valid.")
        return None

    return hasil_operasi

def main():
    # Baca dua gambar untuk dioperasikan
    image1 = cv2.imread('python/captured_image.jpg')
    image2 = cv2.imread('captured_image.jpg')

    if image1 is None or image2 is None:
        print("Gambar tidak ditemukan. Pastikan path gambar benar.")
        return

    # Tampilkan kedua gambar asli
    cv2.imshow('Gambar 1', image1)
    cv2.imshow('Gambar 2', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Panggil fungsi untuk menggabungkan dua gambar dengan operasi boolean
    jenis_operasi = 'xor'  # Ganti dengan 'or', 'xor', atau 'not' sesuai kebutuhan
    hasil_operasi = operasi_boolean(image1, image2, jenis_operasi)

    if hasil_operasi is not None:
        # Tampilkan gambar hasil operasi boolean
        cv2.imshow('Hasil Operasi Boolean', hasil_operasi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
