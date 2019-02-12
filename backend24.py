import math

def calc(lAngka) : 
    lAngka.sort(reverse = True)
    operasi = []
    itungan = lAngka[0]
    for i in range (0,3) :
        plus = itungan + lAngka[i+1]
        minus = itungan - lAngka[i+1]
        times = itungan * lAngka[i+1]
        div = float(itungan / lAngka[i+1])

        jarakplus = abs(24-plus)
        jarakminus = abs(24-minus)
        jaraktimes = abs(24-times)
        jarakdiv = abs(24-div)

        jarak = [jarakplus, jarakminus, jaraktimes, jarakdiv]
        jarak.sort()

        if (jarak[0] == jarakplus) :
            operasi.append("+")
            itungan = plus
        elif (jarak[0] == jarakminus) :
            operasi.append("-")
            itungan = minus
        elif (jarak[0] == jaraktimes) :
            operasi.append("*")
            itungan = times
        elif (jarak[0] == jarakdiv) :
            operasi.append("/")
            itungan = div

    return operasi #hasilnya berbentuk list yang isinya operasi

def calcop(lOperasi) : #menghasilkan total poin dari operasi yang didapat
    poin = 0
    for i in lOperasi :
        if (i == "+") :
            poin = poin + 5
        elif (i == "-") :
            poin = poin + 4
        elif (i == "*") :
            poin = poin + 3
        elif (i == "/") :
            poin = poin + 2
    
    return poin #hasilnya berbentuk integer yang merepresentasikan poin dari operasi

def satuinAngkaOp(lAngka, lOperasi) :
    hasil = (str(lAngka[0]) + lOperasi[0] + str(lAngka[1]) + lOperasi[1] + str(lAngka[2]) + lOperasi[2] + str(lAngka[3]))

    return hasil #hasilnya berbentuk sebuah string ekspresi

def hitungPoinAkhir(hasil, poin) :
    poinAkhir = poin - abs(24 - eval(hasil))

    return poinAkhir #hasilnya berbentuk integer yang merepresentasikan poin akhir