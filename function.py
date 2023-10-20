import numpy as np 
day = input('masukan hari : ').lower()
def checkDay(day):
    if day == 'senin':
        return 'Upacara'
    else:
        return 'tidak upacara'

print(checkDay('selasa'))

def sapa(nama, pesan="!"):
    pesan = 'Halo, ' + nama + pesan
    return pesan 

nama_pengguna = "Alice"
hasil_sapaan = sapa(nama_pengguna)
print(hasil_sapaan)

# parameter sunnah
def sapa(nama = 'tes'):
    print(nama)

# print(sapa(pesan="mangat gan!", nama = 'arief' ))

def kuadrat(angka):
    hasil = angka ** 2
    return hasil

print(f"kuadrat dari 5 adalah {kuadrat(5)}")

sapa('lala')

def hewan():
    def hewan1():
        jenis = 'angsa'
    def hewan2():
        nonlocal jenis
        jenis = "harimau"
    def hewan3():
        global jenis
        jenis = 'gajah'

    jenis = 'ayam'
    hewan1()
    print(f"jenis hewan pertama {jenis}")
    hewan2()
    print(f"jenis hewan pertama {jenis}")
    hewan3()
    print(f"jenis hewan pertama {jenis}")

hewan()
print(f"jenis hewan adalah {jenis}")

data = np.array([1,2,3,4])
print(type(data))