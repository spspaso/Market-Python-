from datetime import datetime

from matplotlib import pyplot as plt

import Proizvod
import Racun

racuni=[]

def loadRacun():
    for line in open("racun.txt", "r").readlines():
        if len(line) > 1:
            racun = str2Racun(line)
            racuni.append(racun)

def str2Racun(line):
    line = line.strip()
    id, proizvodiStr,ukupnaCena,datumStr = line.split('|')
    proizvodiStr=proizvodiStr.split(',')
    proizvodi=[]
    for p in proizvodiStr:
        proizvodi.append(int(p))
    datum=datetime.strptime(datumStr,'%d/%m/%Y')
    r = {
        'id': int(id),
        'proizvodi': proizvodi,
        'cena': float(ukupnaCena),
        'datum': datum
    }
    return r

def saveRacun():
    file = open("racun.txt", "w")
    for racun in racuni:
        file.write(racun2Str(racun))
        file.write("\n")
    file.close()

def racun2Str(r):
    datum=r['datum'].strftime("%d/%m/%Y")
    proizvodi=[str(x) for x in r['proizvodi']]
    proizvodi=",".join(proizvodi)
    return '|'.join([str(r['id']), proizvodi, str(r['cena']),datum])

loadRacun()


def findMaxId():
    maxID=-1
    for racun in racuni:
        if racun['id']>maxID:
            maxID=racun['id']
    return maxID

def generateId():
    if len(racuni)==0:
        return 1
    return  findMaxId()+1

def PrikaziZaraduPoDanima():
    d=['Ponedeljak','Utorak','Sreda','Cetvrtak','Petak','Subota','Nedelja']
    dani=[0,1,2,3,4,5,6]
    zarade=[]
    for dan in dani:
        z=0
        for racun in racuni:
            if racun['datum'].weekday()==dan:
                z+=racun['cena']
        zarade.append(z)
    plt.bar(d, zarade, color='maroon',width=0.4)
    plt.show()


def kupovina():
    racun={}
    racun['proizvodi']=[]
    Proizvod.printProizvod(Proizvod.proizvodi)
    ukupnaCena=0
    racun['datum']=datetime.now()
    while True:
        naziv=input("Unesite naziv proizvoda")
        proizvod=Proizvod.searchProizvodByName(naziv)
        if proizvod==None:
            print("Uneti proizvod ne postoji")
        else:
            kolicina = int(input("Unesite kolicinu proizvoda"))
            if kolicina>proizvod['kolicina']:
                print("Nemamo dovoljno proizvoda")
            else:
                ukupnaCena+=kolicina*proizvod['cena']
                proizvod['kolicina']=proizvod['kolicina']-kolicina
                racun['proizvodi'].append(proizvod['id'])
                print("1. Zavrsi Kupovinu")
                print("2. Dodaj jos proizvoda")
                opt=input("Izaberi opciju: ")
                if opt=="1":
                    break

    racun['id']=generateId()
    racun['cena']=ukupnaCena
    racuni.append(racun)
    Racun.saveRacun()

