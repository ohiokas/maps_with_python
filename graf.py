graf = {
    'Brebes' : ['Tegal', 'Slawi'],
    'Tegal' : ['Brebes', 'Slawi', 'Pemalang'],
    'Slawi' : ['Brebes', 'Tegal', 'Purwokerto'],
    'Purwokerto' : ['Slawi', 'Cilacap', 'Kroya', 'Kebumen', 'Purbalingga'],
    'Pemalang' : ['Tegal', 'Purbalingga', 'Pekalongan'],
    'Purbalingga' : ['Purwokerto', 'Pemalang', 'Banjarnegara'],
    'Pekalongan' : ['Pemalang', 'Kendal'],
    'Cilacap' : ['Purwokerto', 'Kroya'],
    'Kroya' : ['Cilacap', 'Purwokerto', 'Kebumen'],
    'Kebumen' : ['Purwokerto', 'Kroya', 'Purworejo']
}

def perjalanan(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir:
        return [jalur]
    if not awal in graf:
        return []
    seluruh_jalur = []
    for x in graf[awal]:
        if x not in jalur:
            rute = perjalanan(graf, x, akhir, jalur)
            for rute_baru in rute:
                seluruh_jalur.append(rute_baru)
    return seluruh_jalur


def jumlah_rute(jumlah):
    rute = ''
    for x in range(0, len (jumlah)):
        if x < len(jumlah) -1:
            rute += jumlah[x] + '->'
        else:
            rute += jumlah[x]
    return rute
#MAIN PROGRAM
tempat_awal = str(input('Masukkan Kota Asal: '))
tempat_akhir = str(input('Masukkan Kota Tujuan: '))

pencarian = perjalanan(graf, tempat_awal, tempat_akhir)
print('Jumlah Rute: ', len(pencarian))
print()
min = pencarian[0]
max = []
for x in pencarian:
    if len(x) < len(min):
        min = x
    elif len(x) > len(max):
        max = x


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
