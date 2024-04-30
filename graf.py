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
