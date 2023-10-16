def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  
    if from_unit == 'c':
        if to_unit == 'f':
            return (value * 9/5) + 32
        elif to_unit == 'k':
            return value + 273.15
        elif to_unit == 'r': 
            return value * 4/5
    elif from_unit == 'f':
        if to_unit == 'c':
            return (value - 32) * 5/9
        elif to_unit == 'k':
            return (value - 32) * 5/9 + 273.15
        elif to_unit == 'r':
            return (value - 32) * 4/9
    elif from_unit == 'k':
        if to_unit == 'c':
            return value - 273.15
        elif to_unit == 'f':
            return (value - 273.15) * 9/5 + 32
        elif to_unit == 'r':
            return (value - 273.15) * 4/5
    elif from_unit == 'r':
        if to_unit == 'c':
            return value * 5/4
        elif to_unit == 'f':
            return (value * 9/4) + 32
        elif to_unit == 'k':
            return (value * 5/4) + 273.15
    else:
        print('masukan input yang benar')

def menu():
    print('Ketik c untuk Celcius')
    print('Ketik r untuk Reamur')
    print('Ketik f untuk Farenheit')
    print('Ketik k untuk Kelvin')

def longNameConvert(value):
    if value == 'c':
      return 'Celcius'
    elif value == 'f':
      return 'Farenheit'
    elif value == 'k':
      return 'Reamur'

temperature = int(input('masukan suhu awal : '))
menu()
fromTemp = input('Pilihan anda ( awal ) : ')
menu()
toTemp = input('Pilihan anda ( akhir ) : ')
converted_temperature = convert_temperature(temperature, fromTemp, toTemp)
fromTempLong = longNameConvert(fromTemp)
toTempLong = longNameConvert(toTemp)
print(f"suhu yang diinputkan adalah {temperature} derajat {fromTempLong} \nHasil konversi ke {toTempLong} adalah {converted_temperature} {toTempLong}")
