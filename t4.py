data = [
    {
        'nama': 'Dani',
        'masa_kerja': 2
    },
    {
        'nama': 'Duki',
        'masa_kerja': 1
    },
    {
        'nama': 'Duke',
        'masa_kerja': 1
    },
    {
        'nama': 'Deni',
        'masa_kerja': 5,
    },
    {
        'nama': 'Dena',
        'masa_kerja': 6,
    }
]

umr_bandung = 5000000
gaji = [4200000, 4800000, 5300000, 5900000, 6400000]

for i, item in enumerate(data):
    item['gaji'] = gaji[i]

kenaikan_gaji = 1250000
totalGajiKaryawanGanjil = 0
totalGajiKaryawan = 0
totalGajiUnderUMR = 0
lenGajiUnderUMR = 0
avgGajiUnderUMR = 0
totalGajiUMR = 0
lenGajiUMR = 0
avgGajiUMR = 0

for i, item in enumerate(gaji):
    totalGajiKaryawan += item
    if i % 2 != 0:
        totalGajiKaryawanGanjil += item
    elif item < umr_bandung:
        totalGajiUnderUMR += item
        lenGajiUnderUMR += 1
    elif item > umr_bandung:
        totalGajiUMR += item
        lenGajiUMR += 1
    

totalKenaikanGaji = 0
for item in data:
    totalKenaikanGaji += int(item['gaji']) + (kenaikan_gaji * (int(item['masa_kerja'])-1))

avgGajiUnderUMR = totalGajiUnderUMR / lenGajiUnderUMR if lenGajiUnderUMR != 0 else 0
avgGajiUMR = totalGajiUMR / lenGajiUMR if lenGajiUMR != 0 else 0

print("rata-rata gaji tiap index ganjil adalah ", totalGajiKaryawanGanjil)
print("rata-rata gaji karyawan adalah ", totalGajiKaryawan )
print("Rata-rata gaji karyawan yang di bawah UMR:", avgGajiUnderUMR)
print("Rata-rata gaji karyawan yang di atas UMR:", avgGajiUMR)
print("total gaji dengan kenaikan tiap tahun 1.250.000 adalah ", totalKenaikanGaji)
	