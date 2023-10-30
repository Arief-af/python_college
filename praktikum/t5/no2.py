import numpy as np

# Minta input matriks dari pengguna
input_matrix = input('Masukkan matriks 3x3 (pisahkan elemen dengan spasi, dan baris dengan koma): ')
# Konversi input menjadi matriks numpy
matriks = np.array(eval(input_matrix))

# Fungsi untuk mencari angka keberuntungan dalam matriks
def cari_angka_keberuntungan(matriks):
    result = []  # Inisialisasi list hasil
    # Iterasi melalui setiap baris dan indeks baris dalam matriks
    for i, baris in enumerate(matriks):
        min_in_row = np.min(baris)  # Menggunakan np.min untuk menemukan nilai minimum dalam baris
        col_index = np.argmin(baris)  # Menggunakan np.argmin untuk menemukan indeks kolom dari nilai minimum
        # Memeriksa apakah nilai minimum dalam baris juga merupakan nilai maksimum dalam kolom
        if min_in_row == np.max(matriks[:, col_index]):
            result.append(min_in_row)  # Jika ya, tambahkan nilai minimum ke hasil
    return result

# Menggunakan fungsi untuk mencari angka keberuntungan dalam matriks
angka_keberuntungan = cari_angka_keberuntungan(matriks)
# Mencetak hasil
print("Angka Keberuntungan:", angka_keberuntungan)
