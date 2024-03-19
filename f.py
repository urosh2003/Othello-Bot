import copy

def herstanje(pozicija):
    pass

def moguce_pozicije(pozicija, trenutni_igrac):
    pozicije = {}
    if trenutni_igrac==0:
        protivnik="O"
    else:
        protivnik="X"
    for i in range(8):
        for j in range(8):
            if pozicija[i][j] == ' ':
                za_pojesti = potez(pozicija, i,j, protivnik)
                if za_pojesti!=[]:
                    pozicije.update({(i,j): za_pojesti})
    return pozicije

def potez(pozicija, i,j, protivnik):
    za_pojesti = []
    dole = niz_dole(pozicija,i,j,protivnik)
    for pronadjeni in dole:
        za_pojesti.append(pronadjeni)
    gore = niz_gore(pozicija,i,j,protivnik)
    for pronadjeni in gore:
        za_pojesti.append(pronadjeni)
    levo = niz_levo(pozicija,i,j,protivnik)
    for pronadjeni in levo:
        za_pojesti.append(pronadjeni)
    desno = niz_desno(pozicija,i,j,protivnik)
    for pronadjeni in desno:
        za_pojesti.append(pronadjeni)
    
    gore_levo = niz_gore_levo(pozicija,i,j,protivnik)
    for pronadjeni in gore_levo:
        za_pojesti.append(pronadjeni)
    gore_desno = niz_gore_desno(pozicija,i,j,protivnik)
    for pronadjeni in gore_desno:
        za_pojesti.append(pronadjeni)

    dole_levo = niz_dole_levo(pozicija,i,j,protivnik)
    for pronadjeni in dole_levo:
        za_pojesti.append(pronadjeni)
    dole_desno = niz_dole_desno(pozicija,i,j,protivnik)
    for pronadjeni in dole_desno:
        za_pojesti.append(pronadjeni)   
    
    return za_pojesti        


def niz_dole(pozicija, i,j,protivnik):
    potencijalni = []
    for i in range(i+1, 8):
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []

def niz_gore(pozicija, i,j,protivnik):
    potencijalni = []
    for i in range(i-1, -1, -1):
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []

def niz_levo(pozicija, i,j,protivnik):
    potencijalni = []
    for j in range(j-1, -1, -1):
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []
def niz_desno(pozicija, i,j,protivnik):
    potencijalni = []
    for j in range(j+1, 8):
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []

def niz_gore_levo(pozicija, i,j,protivnik):
    potencijalni = []
    for j in range(j-1, -1, -1):
        i-=1
        if i==-1: break
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []
def niz_gore_desno(pozicija, i,j,protivnik):
    potencijalni = []
    for j in range(j+1, 8):
        i-=1
        if i==-1: break
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []

def niz_dole_levo(pozicija, i,j,protivnik):
    potencijalni=[]
    for j in range(j-1, -1, -1):
        i+=1
        if i==8: break
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []
def niz_dole_desno(pozicija, i,j,protivnik):
    potencijalni=[]
    for j in range(j+1, 8):
        i+=1
        if i==8: break
        if pozicija[i][j]==protivnik:
            potencijalni.append((i,j))
        elif pozicija[i][j]==' ':
            return []
        else:
            return potencijalni
    return []





def pojedi(pozicija, spisak, mesto, znak):
    novapoz= copy.deepcopy(pozicija)
    a,b = mesto
    novapoz[a][b] = znak
    if spisak!=[] and spisak!=None:
        for par in spisak:
            i,j = par
            novapoz[i][j]=znak
    return novapoz
