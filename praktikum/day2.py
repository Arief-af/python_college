def app():
    a = input('masukan angka : ')
    if a%2 == 0:
        print(f"{a} adalah bilangan genap")
    else:
        print(f"{a} adalah bilangan ganjil")

toggle = 'yes'
while(toggle == 'yes'):
    app()
    toggle = input('input lagi yes/no : ')
