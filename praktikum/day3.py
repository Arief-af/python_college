data = []

def store(jumlah_mhs, jumlah_matkul):
    for item in range(jumlah_mhs):
        nilaiMatkul = []  
        data.append({
            'name': input(f'masukan data nama ke-{item} : ')
        })
        for itemMatkul in range(jumlah_matkul):
           nilaiMatkul.append(input(f'nilai matkul {data[item]["name"]} ke-{itemMatkul} : '))
        data[item]['nilai_matkul'] = nilaiMatkul

def avg():
    for item in data:
        avgValue = 0
        for itemAvg in item['nilai_matkul']:
            avgValue = avgValue + int(itemAvg)
        item['nilai_avg'] = avgValue / len(item['nilai_matkul'])

def display_data():
    for item in data:
        print(f"\nName: {item['name']}")
        print("Nilai Matkul:")
        for i, nilai in enumerate(item['nilai_matkul']):
            print(f"  Matkul {i + 1}: {nilai}")
        print(f"Nilai Average: {item['nilai_avg']}")

jumlah_mhs = int(input('Masukan banyak mahasiswa : '))
jumlah_matkul = int(input('Masukan banyak matkul : '))

store(jumlah_mhs, jumlah_matkul)
avg()
display_data()