import tabulate
def loadProizvod():
    for line in open("proizvod.txt", "r").readlines():
        if len(line) > 1:
            proizvod = str2Proizvod(line)
            proizvodi.append(proizvod)

def saveProizvod():
    file = open("proizvod.txt", "w")
    for proizvod in proizvodi:
        file.write(proizvod2str(proizvod))
        file.write("\n")
    file.close()


def str2Proizvod(line):
    line = line.strip()
    id, naziv,kolicina,cena = line.split('|')
    p = {
        'id': int(id),
        'naziv': naziv,
        'kolicina': int(kolicina),
        'cena': float(cena)
    }
    return p

def proizvod2str(p):
    return '|'.join([str(p['id']), p['naziv'],str(p['kolicina']),str(p['cena'])])


def sortirajProzivode():
    proizvodi.sort(key = lambda x: x['cena'],reverse=True)
    printProizvod(proizvodi)


def searchProizvodByName(naziv):
    for p in proizvodi:
        if p['naziv'].upper() == naziv.upper():
            return p
    return None


def searchProizvod(id):
    for p in proizvodi:
        if p['id']==id:
            return p
    return  None

def promeniCenuProizvoda():
    printProizvod(proizvodi)
    sifra =int(input("Unesite sifru proizvoda"))
    p=searchProizvod(sifra)
    if p==None:
        print("Uneli ste sifru proizvoda koji ne postoji")
        return
    cena=float(input("Unesite novu cenu: "))
    p['cena']=cena


def printProizvod(proizvodi):
    data=[]
    for p in proizvodi:
        d=[]
        d.append(p['id'])
        d.append(p['naziv'])
        d.append(p['kolicina'])
        d.append(p['cena'])
        data.append(d)
    print(tabulate.tabulate(data, headers=["Id", "Naziv", "Kolicina","Cena"]))
proizvodi = []
loadProizvod()



