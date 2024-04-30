#bagian Zaki

#bagian Yosi

#bagian Vikas
r = [
    'Rute Tercepat : ', jumlah_rute(min),
    '',
    'Rute Terlambat: ', jumlah_rute(max),
    '',
    'Daftar Rute Yang Dapat Dilewati: ']

for x in r:
    print(x)
for x in range(0, len(pencarian)):
    print('Rute',x+1,':')
    print(jumlah_rute(pencarian[x]))
    print()
