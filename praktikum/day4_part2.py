# init variable untuk menampung hasil data akhir
dataPelanggan = []
dataBarang = []
dataSupplier = []

# function untuk input data barang yang membeli return berbentuk dict
def barang():
    kode = input('Input kode barang : ')
    nama = input('Input nama barang : ')
    harga = input('Input harga barang : ')
    jumlah_beli = input('Input jumlah beli barang : ')
    dataBarangObject = {
        'kode': kode,
        'nama': nama,
        'harga': harga,
        'jumlah_beli': jumlah_beli,
    }
    return dataBarangObject

# function untuk input data pelanggan yang membeli return berbentuk dict
def pelanggan():
    kode = input('Input kode pelanggan : ')
    nama = input('Input nama : ')
    alamat = input('Input alamat : ')

    dataPelangganObject = {
        'kode': kode,
        'nama': nama,
        'alamat': alamat,
        'list_barang': [],  # Initialize as an empty list
        'supplier': []  # Initialize as an empty list
    }
    return dataPelangganObject

# function untuk input data supplier yang membeli return berbentuk dict
def supplier():
    kode = input('Input kode supplier : ')
    nama = input('Input nama : ')
    status = input('Input status : ')
    kota = input('Input kota : ')

    dataSupplierObject = {
        'kode': kode,
        'nama': nama,
        'status': status,
        'kota': kota
    }

    return dataSupplierObject

# init variable untuk menampung jumlah pelanggan yang dimasukan
pelangganCount = int(input('Masukan jumlah pelanggan yang akan dimasukan: '))

# looping sesuai dengan pelangganCount
for i in range(pelangganCount):
    pelanggan_data = pelanggan()
    # init variable untuk menampung jumlah barang yang dimasukan
    barangCount = int(input('Masukan jumlah barang yang akan dimasukan: '))
    # looping sesuai dengan barangCount
    for j in range(barangCount):
        # memasukan data barang ke array list_barang yang ada pada pelanggan_data 
        pelanggan_data['list_barang'].append(barang())  
    # init variable untuk menampung jumlah supplier yang dimasukan
     # looping sesuai dengan supplierCount
    supplierCount = int(input('Masukan jumlah supplier yang akan dimasukan: '))
    for k in range(supplierCount):
        # memasukan data supplier ke array list_barang yang ada pada pelanggan_data
        pelanggan_data['supplier'].append(supplier())  
    # memasukan data pelanggan_data ke array dataPelanggan
    dataPelanggan.append(pelanggan_data)

print()
# print dataPelanggan 
for item in dataPelanggan:
    print(f'Data Pelanggan')
    print(f'Kode Pelanggan : {item["kode"]}')
    print(f'Nama Pelanggan : {item["nama"]}')
    print(f'Alamat : {item["alamat"]}')
    
    print(f'Supplier Data:')
    # print semua data supplier yang ada pada item['supplier']
    for itemSpl in item['supplier']:
        print(f'supplier code: {itemSpl["kode"]}')
        print(f'Status: {itemSpl["status"]}')
        print(f'Kota: {itemSpl["kota"]}')
    # print semua data barang yang ada pada item['list_barang']
    print(f'Data Barang')
    for itemBrg in item['list_barang']:
        print(f'Kode barang: {itemBrg["kode"]}')
        print(f'Nama Barang: {itemBrg["nama"]}')
        print(f'Harga: {itemBrg["harga"]}')
        print(f'Jumlah: {itemBrg["jumlah_beli"]}')
    print()

# init variable untuk menampung data barang yang terbanyak
max_barang_count = 0
# init variable untuk menampung data pelanggan yang memiliki barang terbanyak
max_barang_pelanggan = None

# perulangan untuk mencari data pelanggan yg memiliki barang terbanyak
for pelanggan_data in dataPelanggan:
    barang_count = len(pelanggan_data['list_barang'])
    # jika pelanggan ini memiliki barang lebih dari max_barang_count maka max_barang_count, max_barang_pelanggan diganti dengan data perulangan itu
    if barang_count > max_barang_count:
        max_barang_count = barang_count
        max_barang_pelanggan = pelanggan_data

# jika max_barang_pelanggan tidak Note maka print data tersebut
if max_barang_pelanggan is not None:
    print("Pelanggan dengan jumlah barang terbanyak:")
    print(f'Kode Pelanggan: {max_barang_pelanggan["kode"]}')
    print(f'Nama Pelanggan: {max_barang_pelanggan["nama"]}')
    print(f'Alamat: {max_barang_pelanggan["alamat"]}')
    print(f'Jumlah Barang: {max_barang_count}')
else:
    # jika tidak
    print("Tidak ada pelanggan dengan data barang.")

# init variable untuk menampung data barang yang terbanyak
max_total_transaksi = 0
# init variable untuk menampung data pelanggan yang memiliki transaksi terbanyak
max_transaksi_pelanggan = None

for pelanggan_data in dataPelanggan:
    total_transaksi = 0
    # menghitung total harga transaksi
    for barang_data in pelanggan_data['list_barang']:
        harga = float(barang_data['harga'])
        jumlah_beli = int(barang_data['jumlah_beli'])
        total_transaksi += harga * jumlah_beli

    # jika pelanggan ini memiliki transaksi lebih dari max_total_transaksi maka max_total_transaksi, max_transaksi_pelanggan diganti dengan data perulangan itu
    if total_transaksi > max_total_transaksi:
        max_total_transaksi = total_transaksi
        max_transaksi_pelanggan = pelanggan_data

# jika max_transaksi_pelanggan tidak Note maka print data tersebut
if max_transaksi_pelanggan is not None:
    print("Pelanggan dengan transaksi terbesar:")
    print(f'Kode Pelanggan: {max_transaksi_pelanggan["kode"]}')
    print(f'Nama Pelanggan: {max_transaksi_pelanggan["nama"]}')
    print(f'Alamat: {max_transaksi_pelanggan["alamat"]}')
    print(f'Total Transaksi: ${max_total_transaksi:.2f}')
else:
    # jika
    print("Tidak ada pelanggan dengan transaksi.")