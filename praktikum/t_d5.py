# import numpy as np

# gajiInput = input('Masukkan jam kerja (pisahkan dengan spasi): ')
# gaji = np.fromstring(gajiInput, dtype=int, sep=' ')
# def filter(min, max):
#     global gaji
#     filterData = []
#     for item in gaji:
#         if item != min and item != max:
#             filterData.append(item)
#     return filterData

# print(f"salary = {gaji}")
# print(f"Output: {np.mean(filter(np.min(gaji), np.max(gaji)))}")

# def cari_angka_keberuntungan(matriks):
#     result = []
#     for i, baris in enumerate(matriks):
#         min_in_row = min(baris)
#         col_index = baris.index(min_in_row)
#         if min_in_row == max(matriks[j][col_index] for j in range(len(matriks))):
#             result.append(min_in_row)
#     return result

# matriks = [
#     [3, 7, 8],
#     [9, 11, 13],
#     [15, 17, 19]
# ]

# angka_keberuntungan = cari_angka_keberuntungan(matriks)
# print("Angka Keberuntungan:", angka_keberuntungan)




    