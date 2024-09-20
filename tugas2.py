panjang = float(input('masukkan panjang ruangan : '))
lebar = float(input('masukkan lebar ruangan : '))
satuan = input('masukkan satuan (meter/inci) : ')
luas = panjang * lebar
print(f'''
luas ruangan dengan panjang {float(panjang)} dan lebar {float(lebar)} adalahh {luas} {satuan}     
''')