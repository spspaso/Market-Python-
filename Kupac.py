import  datetime

kupci=[]

def str2Kupac(line):
    line = line.strip()
    userName, password, firstName, lastName = line.split("|")
    kupac = {
        'username': userName,
        'password': password,
        'firstname': firstName,
        'lastname': lastName,
    }
    return kupac


def login():
    username=input("Unesite korisnicko ime")
    password=input("Unesite password")
    for kupac in kupci:
        if kupac['username']==username and kupac['password']==password:
            return  kupac
    return None


def loadKupci():
    for line in open("kupac.txt", "r").readlines():
        if len(line) > 1:
            line=line.strip()
            kupac = str2Kupac(line)
            kupci.append(kupac)

def kupac2str(p):
    linija=p['username']+"|"+p['password']+"|"+p['firstname']+"|"+p['lastname']
    return linija

def saveKupci():
    file = open("kupac.txt", "w")
    for k in kupci:
        file.write(kupac2str(k))
        file.write("\n")
    file.close()

loadKupci()
