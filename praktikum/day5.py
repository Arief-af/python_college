# happy number

angka = input('number : ')

def angka_bahagia(n):
    temp = set()
    while n != 1 and n not in temp:
        temp.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


if angka_bahagia(angka):
    print(f"{angka} adalah happy number" )
else:
    print(f"{angka} adalah bukan happy number" )
