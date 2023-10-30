# Mengimpor library yang diperlukan
import numpy as np

# Meminta input dari pengguna berupa gaji
gajiInput = input('Masukkan gaji (pisahkan dengan spasi): ')
# Mengonversi input menjadi array numpy
gaji = np.fromstring(gajiInput, dtype=int, sep=' ')

# Fungsi untuk menyaring data gaji yang tidak termasuk nilai minimum dan maksimum
def filter(min, max):
    global gaji  # Menggunakan variabel global gaji
    filterData = []
    # Iterasi melalui setiap item dalam array gaji
    for item in gaji:
        # Menyaring nilai yang bukan minimum atau maksimum
        if item != min and item != max:
            filterData.append(item)
    # Mengembalikan data yang sudah disaring
    return filterData

# Mencetak nilai gaji awal
print(f"Gaji = {gaji}")
# Mencetak rata-rata dari data gaji setelah disaring
print(f"Output: {np.mean(filter(np.min(gaji), np.max(gaji)))}")
