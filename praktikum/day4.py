
def hitungKalori(bb,tb,u, gender):
    gender = gender.lower()
    if gender == 'pria':
        result = lambda : 66 + (13.7*bb)+ (5*tb)-(6.8*u)
        return f"Kalori yang dibutuhkan oleh anda sebesar {result}"
    elif gender == 'wanita':
        result = lambda :  665 + (9.6*bb)+ (1.8*tb)-(4.7*u)
        return f"Kalori yang dibutuhkan oleh anda sebesar {result}"
    else:
        result = 'gender tidak valid'
        return result
    
pria = lambda bb, tb, u: 66 + (13.7*bb)+ (5*tb)-(6.8*u)
wanita = lambda bb, tb, u:  665 + (9.6*bb)+ (1.8*tb)-(4.7*u)

gender = input('Masukan gender anda (pria/wanita) : ')
beratBadan = float(input('Masukan berat badan anda : '))
tinggiBadan = float(input('Masukan tinggi badan anda : '))
usia = float(input('Masukan usia anda : '))

print('Using lambda')
if gender.lower() == 'pria':
    print(f"Kalori yang dibutuhkan oleh anda sebesar {pria(beratBadan, tinggiBadan, usia)}")
else:
    print(f"Kalori yang dibutuhkan oleh anda sebesar {wanita(beratBadan, tinggiBadan, usia)}")
print('Using def')
print(hitungKalori(beratBadan, tinggiBadan, usia, gender))