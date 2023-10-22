mahasiswa = [
    {
        'nama': 'diash',
        'status': 'aktif'
    },
    {
        'nama': 'firdaus',
        'status': 'aktif'
    },
    {
        'nama': 'lisa',
        'status': 'aktif'
    },
    {
        'nama': 'Cristiana',
        'status': 'tidak_aktif'
    },
    {
        'nama': 'yusuf',
        'status': 'tidak_aktif'
    },
    {
        'nama': 'miftahudin',
        'status': 'tidak_aktif'
    },
]


def printData(array, message):
    print('------------------------------')
    print(message)
    for item in array:
        print('------------------------------')
        print(f"Nama   : {item['nama']}")
        print(f"Status : {item['status']}")
        print('------------------------------')
    print('\n')


i = 0
mahasiswa_aktif = []
mahasiswa_tidak_aktif = []

while i < len(mahasiswa):
    if mahasiswa[i]['status'] == 'aktif':
        mahasiswa_aktif.append(mahasiswa[i])
    else:
        mahasiswa_tidak_aktif.append(mahasiswa[i])
    i = i + 1

printData(mahasiswa_aktif, 'Data mahasiswa aktif : ')
printData(mahasiswa_tidak_aktif, 'Data mahasiswa tidak aktif : ')
