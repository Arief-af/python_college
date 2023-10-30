# Mengimpor library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung keuntungan maksimal dari harga saham
def max_profit(prices):
    # Menangani kasus jika input kosong atau hanya terdapat satu harga saham
    if prices is None or len(prices) < 2:
        return 0

    # Inisialisasi variabel keuntungan maksimal dan harga saham minimal
    max_profit = 0
    min_price = prices[0]

    # Iterasi melalui setiap harga saham
    for price in prices:
        # Memperbarui harga saham minimal
        min_price = min(min_price, price)
        # Menghitung keuntungan maksimal pada titik ini
        max_profit = max(max_profit, price - min_price)

    # Mengembalikan keuntungan maksimal
    return max_profit

# Contoh penggunaan:
# Mengambil input harga saham dari pengguna
price_input = input('Masukkan harga saham (pisahkan dengan spasi): ')
# Mengonversi input menjadi array numpy
prices = np.fromstring(price_input, dtype=int, sep=' ')

# Menghitung dan mencetak keuntungan maksimal
result = max_profit(prices)
print(f"Keuntungan maksimal yang bisa didapat adalah: {result}")

# Visualisasi grafik harga saham dan titik pembelian/jualan
# Plot harga saham
plt.plot(prices, label='Harga Saham')
# Menentukan hari pembelian
buy_day = np.argmin(prices)
# Menentukan hari penjualan
sell_day = buy_day + np.argmax(prices[buy_day:])
# Menandai titik pembelian dan penjualan pada grafik
plt.scatter(buy_day, prices[buy_day], color='green', label='Beli')
plt.scatter(sell_day, prices[sell_day], color='red', label='Jual')
# Menampilkan legenda, judul, dan label sumbu pada grafik
plt.legend()
plt.title(f'Grafik harga saham dan Titik Pembelian/jualan')
plt.xlabel('Hari')
plt.ylabel('Harga Saham')
# Menampilkan grafik
plt.show()
