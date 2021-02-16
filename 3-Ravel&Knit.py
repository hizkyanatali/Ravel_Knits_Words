'''
fungsi ravel(...) akan mengurai string.
'''

print('~' * 20, "3. Ravelling and Knitting Words", '~' * 20)


def ravel(kata):
    hasil = ''
    for i in range(len(kata)+1):
        hasil += kata[0:i]
    return hasil


print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))


print('~'*50)
'''
Sedangkan fungsi knit(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya.
# hasil pemikiran = panjang dari input pasti:
# 1 untuk asal kata 1 huruf
# 3 untuk asal kata 2 huruf
# 6 untuk asal kata 3 huruf
# 10 untuk asal kata 4 huruf
# 15 untuk asal kata 5 huruf
# 21 untuk asal kata 6 huruf
# 28 untuk asal kata 7 huruf
# 36 untuk asal kata 8 huruf
# 45 untuk asal kata 9 huruf
# 55 untuk asal kata 10 huruf <karena Purwadhika ada 10 huruf, analisis sampai 10 huruf saja>
Pengerjaan tugas ini tidak menggunakan handling error
'''


def knit(kata):
    hasil = ''
    if len(kata) == 1:  # untuk input 1 huruf maka keluarannya huruf itu sendiri
        hasil = kata[0]
    elif len(kata) == 3:  # untuk input 3 huruf maka keluarannya 2 huruf
        hasil = kata[(len(kata) - 2):len(kata)]
    elif len(kata) == 6:  # untuk input 6 huruf maka keluarannya 3 huruf
        hasil = kata[(len(kata) - 3):len(kata)]
    elif len(kata) == 10:  # untuk input 10 huruf maka keluarannya 4 huruf
        hasil = kata[(len(kata) - 4):len(kata)]
    elif len(kata) == 15:  # untuk input 15 huruf maka keluarannya 5 huruf
        hasil = kata[(len(kata) - 5):len(kata)]
    elif len(kata) == 21:  # untuk input 21 huruf maka keluarannya 6 huruf
        hasil = kata[(len(kata) - 6):len(kata)]
    elif len(kata) == 28:  # untuk input 28 huruf maka keluarannya 7 huruf
        hasil = kata[(len(kata) - 7):len(kata)]
    elif len(kata) == 36:  # untuk input 36 huruf maka keluarannya 8 huruf
        hasil = kata[(len(kata) - 8):len(kata)]
    elif len(kata) == 45:  # untuk input 45 huruf maka keluarannya 9 huruf
        hasil = kata[(len(kata) - 9):len(kata)]
    elif len(kata) == 55:  # untuk input 45 huruf maka keluarannya 10 huruf
        hasil = kata[(len(kata) - 10):len(kata)]
    return hasil


print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))
