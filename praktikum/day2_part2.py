data = []
toggle = 'yes'

def checker():
    for item in data:
        index_nilai = int(item['nilai_akhir'])
        if index_nilai < 45:
            item['index'] = 'E'
        elif index_nilai > 45 < index_nilai < 50:
            item['index'] = 'D'
        elif index_nilai > 50 < index_nilai < 60:
            item['index'] = 'C'
        elif index_nilai > 60 < index_nilai < 70:
            item['index'] = 'B'
        else:
            item['index'] = 'A'

def store():
    data.append(
        {
            'nama': input('Masukkan nama anda: '),
            'NIM': input('Masukkan NIM anda: '),
            'mata_kuliah': input('Masukkan mata kuliah anda: '),
            'nilai_akhir': input('masukan nilai akhir anda : '),
            'index': 'default'
        }
    )

def index_data():
    for item in data:
        print(f'nama : {item["nama"]}')
        print(f'NIM : {item["NIM"]}')
        print(f'mata_kuliah : {item["mata_kuliah"]}')
        print(f'nilai_akhir : {item["nilai_akhir"]}')
        print(f'index :{item["index"]}')

while toggle == 'yes':
    store()
    checker()
    toggle = input('ingin masukan data lagi? yes/no : ')


print(data) 
