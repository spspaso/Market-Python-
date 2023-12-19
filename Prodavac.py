import  datetime

def str2Prodavac(line):
    line = line.strip()
    userName, password, firstName, lastName = line.split("|")
    prodavac = {
        'username': userName,
        'password': password,
        'firstname': firstName,
        'lastname': lastName,
    }
    return prodavac

def loadProdavci():
    for line in open("prodavac.txt", "r").readlines():
        if len(line) > 1:
            line=line.strip()
            prodavac = str2Prodavac(line)
            prodavci.append(prodavac)

def prodavac2str(p):
    linija=p['username']+"|"+p['password']+"|"+p['firstname']+"|"+p['lastname']
    return linija

def saveProdavci():
    file = open("prodavac.txt", "w")
    for p in prodavci:
        file.write(prodavac2str(p))
        file.write("\n")
    file.close()


def login():
    username = input("Unesite korisnicko ime")
    password = input("Unesite password")
    for prodavac in prodavci:
        if prodavac['username'] == username and prodavac['password'] == password:
            return prodavac
    return None

prodavci=[]

loadProdavci()