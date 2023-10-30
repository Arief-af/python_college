import numpy as np
import matplotlib.pyplot as plt

karyawan = int(input('Masukkan jumlah karyawan: '))
jamKerja = input('Masukkan jam kerja (pisahkan dengan spasi): ')
karyawanArray = np.array([i for i in range(karyawan)])
jamKerjaArray = np.fromstring(jamKerja, dtype=int, sep=' ')
data = np.vstack((karyawanArray, jamKerjaArray))
target = int(input('Target: '))

jumlahKaryawanTarget = 0
jumlahKaryawanTidakTarget = 0
karyawanListTarget = []
karyawanListTidakTarget = []

for i, jamItem in enumerate(data[1]):
    if jamItem >= target:
        jumlahKaryawanTarget += 1
        karyawanListTarget.append(i + 1)
    else:
        jumlahKaryawanTidakTarget += 1
        karyawanListTidakTarget.append(i + 1)

print(f'Jumlah karyawan yang mencapai target: {jumlahKaryawanTarget}')
print(f'Jumlah karyawan yang tidak mencapai target: {jumlahKaryawanTidakTarget}')

# Plotting the data
plt.bar(['mencapat/melebihi target','tidak mencapat/melebihi target'], [jumlahKaryawanTarget, jumlahKaryawanTidakTarget], color=['blue', 'red'])
plt.xlabel('Status Karyawan')
plt.ylabel('Jumlah Karyawan')
plt.title('Perbandingan Karyawan yang Mencapai/Melebihi Target dan Tidak')
plt.show()