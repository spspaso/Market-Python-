import Kupac
import  Prodavac
import  Proizvod
import Racun

def ProdavacMeni():
    print("1. Prikazi sve proizvode ")
    print("2. Promeni cenu proizvoda")
    print("3. Pretraga proizvoda po imenu")
    print("4. Sortiraj proizvode po ceni")
    print("5. Prodaj prozvod ")
    print("6. Grafik: ")
    print("0. IZADJI")
    opcija = input("Unesite opciju: ")
    return opcija

def KupacMeni():
    print("1. Prikazi sve proizvode ")
    print("2. Pretraga proizvoda po imenu")
    print("3. Sortiraj proizvode po ceni")
    print("4. Kupi prozvod ")
    print("0. IZADJI")
    opcija = input("Unesite opciju: ")
    return opcija

def ProdavacHandler():
    option = ''
    while option != '0':
        option = ProdavacMeni()
        if option == '1':
            Proizvod.printProizvod(Proizvod.proizvodi)
        elif option == '2':
            Proizvod.promeniCenuProizvoda()
        elif option == '3':
            naziv = input("Unesite naziv")
            p = Proizvod.searchProizvodByName(naziv)
            if p != None:
                print(p)
        elif option == '4':
            Proizvod.sortirajProzivode()
        elif option == '5':
            Racun.kupovina()
        elif option == '6':
            Racun.PrikaziZaraduPoDanima()



def KupacHandler():
    option = ''
    while option != '0':
        option = KupacMeni()
        if option == '1':
            Proizvod.printProizvod(Proizvod.proizvodi)
        elif option == '2':
            naziv = input("Unesite naziv")
            p = Proizvod.searchProizvodByName(naziv)
            if p != None:
                print(p)

        elif option == '3':
            Proizvod.sortirajProzivode()

        elif option == '4':
            Racun.kupovina()


def meni():
    print("1. Prikazi sve proizvode ")
    print("2. Promeni cenu proizvoda")
    print("3. Pretraga proizvoda po imenu")
    print("4. Sortiraj proizvode po ceni")
    print("5. Prodaj prozvod ")
    print("6. Grafik: ")
    print("0. IZADJI")
    opcija=input("Unesite opciju: ")
    return opcija

def main():
    opt=""
    while True:
        print("1. Uloguj se kao kupac")
        print("2. Uloguj se kao prodavac")
        opt=input("izaberite opciju: ")
        if opt=="1" or opt=="2":
            break
    if opt=="2":
        prodavac=Prodavac.login()
        while prodavac==None:
            print("Uneli ste pogresno korisnicko ime ili lozinku")
            prodavac = Prodavac.login()
        ProdavacHandler()
    else:
        kupac= Kupac.login()
        while kupac == None:
            print("Uneli ste pogresno korisnicko ime ili lozinku")
            kupac = Kupac.login()
        KupacHandler()

    print("Odjava iz sistema")
    Proizvod.saveProizvod()
    Racun.saveRacun()


main()