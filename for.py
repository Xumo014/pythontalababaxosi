n = 0
talaba_soni=int(input('Nechta talaba bor'))
oraliq_soni=int(input('Oraliqlar sonini kiriting='))
for talaba in range(talaba_soni):
    yigindi=0
    n = n + 1
    ism=(input(f"{n}-talabani ismini kiriting>"))
    a = 0
    for baho in range(oraliq_soni):
        a+=1
        b = int(input(f"{ism}ning {a}- nazorat ishi uchun baxosi>"))

        yigindi = yigindi + b
    natija=yigindi/oraliq_soni
    print(f"{ism}ning ballarining o'rta qiiymati {natija}ga teng")


