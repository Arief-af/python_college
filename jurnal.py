from datetime import datetime

KTP = [{
    'NIK': '232262152022',
    'name': 'Hokage Ketiga',
    'Alamat': 'Konoha',
}, {
    'NIK': '232362152022',
    'name': 'Danzo',
    'Alamat': 'Konoha',
}]

for itemKTP in KTP:
  if (itemKTP['NIK']) == '232262152022':
    itemKTP['role'] = 'admin'
  else:
    itemKTP['role'] = 'rakyat'
    itemKTP['status'] = 'verify'

state = {'name': 'user'}
log = []

uangNegara = 10000000000

print('Masuk ke Website Dashboard Keuangan Negara')
print('scanning KTP....')
print('getting data...')
login = input('Type your NIK : ')


def checkLoginAdmin():
  for item in KTP:
    if item['NIK'] == login and item['role'] == 'admin':
      print(item['NIK'])
      state['name'] = item['name']
      return True
  return False


def checkLoginRakyat():
  for item in KTP:
    if item['NIK'] == login and item['status'] == 'verify':
      print(item['NIK'])
      state['name'] = item['name']
      return True
  return False

def pengeluaran(ParamPengeluaran, deskripsi):
  global uangNegara
  uangNegara -= ParamPengeluaran
  log.append({
      'name': state['name'],
      'uang negara': uangNegara,
      'pengeluaran': ParamPengeluaran,
      'deskripsi': deskripsi,
      'time_stamps': datetime.now()
  })
  print('Log Has been created')
  print('---------------------------------------------------------')


def pemasukan(ParamPemasukan, deskripsi):
  global uangNegara
  uangNegara += ParamPemasukan
  log.append({
      'name': state['name'],
      'uang negara': uangNegara,
      'pemasukan': ParamPemasukan,
      'deskripsi': deskripsi,
      'time_stamps': datetime.now()
  })
  print('Log Has been created')
  print('---------------------------------------------------------')


if checkLoginAdmin():
  print('Welcome', state['name'])
  inputPemasukan = input('Apakah ada pemasukan (yes/no): ')

  def methodPemasukan():
    print('---------------------------------------------------------')
    print('Masukan Data Pemasukan Keuangan Negara')
    FormPemasukan = int(input('masukan jumlah uang : '))
    FormDeskripsi = input('Dari mana uang tersebut : ')
    pemasukan(FormPemasukan, FormDeskripsi)

  def methodPengeluaran():
    print('---------------------------------------------------------')
    print('Masukan Data Pemasukan Keuangan Negara')
    FormPengeluaran = int(input('masukan jumlah uang : '))
    FormDeskripsi = input('Dari mana uang tersebut : ')
    pengeluaran(FormPengeluaran, FormDeskripsi)

  while (inputPemasukan != 'no'):
    methodPemasukan()
    inputPemasukan = input('Apakah ada pemasukan lagi? (yes/no): ')

  inputPengeluaran = input('Apakah ada pengeluaran? (yes/no) ')
  while (inputPengeluaran != 'no'):
    methodPengeluaran()
    inputPengeluaran = input('Apakah ada pengeluaran lagi? (yes/no): ')
  print('keluar dari website')
else:
  print('akses di tolak')
  print('keluar dari website')


def readData():
  print('data informasi keuangan negara : ')
  for data in log:
    print(log)
  print('---------------end----------------')


print(
    'Masuk ke dalam website Informasi Keuangan Negara Khusus Rakyat Indonesia')
FormReadData = input(
    'Apakah anda ingin melihat data Informasi Keuangan Negara Rakyat indonesia? (yes/no) '
)

print('scanning KTP....')
print('getting data...')
login = input('Type your NIK : ')
if FormReadData == 'yes':
  if checkLoginRakyat():
    readData()
