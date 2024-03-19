import heuristika
import f
import minmax

from enum import Enum
 
class Slova(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5 
    G = 6
    H = 7

pozicija = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],]

def ispis(pozicija):
    i=0
    print("| |1|2|3|4|5|6|7|8")
    for red in pozicija:
        print(end="|"+Slova(i).name+"|")
        i+=1
        for polje in red:
            print(polje,end=":")
        print()
    print("Trenutno stanje ima vrednost: " + str(heuristika.dynamic_heuristic_evaluation_function(pozicija)))

a=input("Unesite 1 da igrate prvi ili 2 da igrate drugi >>")
if a=="1":
    igrac=0
    while True:
        print("====================================================")
        ispis(pozicija)
        moguce = f.moguce_pozicije(pozicija,igrac)
        if moguce == {}:
            break

        if igrac==0:
            print("Moguce opcije su: ")
            for potez in moguce:
                x, y = potez
                print(Slova(x).name + str(y+1),end=" ")
            print()
            unos = input("Unesite zeljeno polje (ili 0 za izlaz): >>").upper()
            if unos == "0":
                print("Izlazak iz aplikacije")
                exit()
            if len(unos)!=2 or (unos[1].isdigit()==False) or (unos[0].isalpha()==False) or (unos[0]>"H") or ((Slova[unos[0]].value,int(unos[1])-1) not in moguce):
                print("Los unos")
            else:
                pozicija = f.pojedi(pozicija, moguce.get((Slova[unos[0]].value,int(unos[1])-1)),(Slova[unos[0]].value,int(unos[1])-1), "X")
                igrac=1
        else:
            minvrednost = 99999999
            najbpotez = 0, 0
            dubina = 5 - (len(moguce)//7)
            for potez in moguce:
                vrednost = minmax.minmax(f.pojedi(pozicija, moguce.get(potez),potez, "O"), 0, -99999999, 99999999, dubina)
                ##print(vrednost)
                if vrednost < minvrednost:
                    minvrednost = vrednost
                    najbpotez = potez
            pozicija = f.pojedi(pozicija, moguce.get(najbpotez),najbpotez, "O")
            igrac=0 
elif a=="2":
    igrac=0
    while True:
        print("====================================================")
        ispis(pozicija)
        moguce = f.moguce_pozicije(pozicija,igrac)
        if moguce == {}:
            break

        if igrac==0:
            maxvrednost = -99999999
            najbpotez = 0, 0
            dubina = 5 - (len(moguce)//7)
            for potez in moguce:
                vrednost = minmax.minmax(f.pojedi(pozicija, moguce.get(potez),potez, "X"), 1, -99999999, 99999999, dubina)
                print(vrednost)
                if vrednost > maxvrednost:
                    maxvrednost = vrednost
                    najbpotez = potez

            pozicija = f.pojedi(pozicija, moguce.get(najbpotez),najbpotez, "X")
            igrac=1
        else:
            print("Moguce opcije su: ")
            for potez in moguce:
                x, y = potez
                print(Slova(x).name + str(y+1),end=" ")
            print()
            unos = input("Unesite zeljeno polje (ili 0 za izlaz): >>").upper()
            if unos == "0":
                print("Izlazak iz aplikacije")
                exit()
            if len(unos)!=2 or (unos[1].isdigit()==False) or (unos[0].isalpha()==False) or (unos[0]>"H") or ((Slova[unos[0]].value,int(unos[1])-1) not in moguce):
                print("Los unos")
            else:
                pozicija = f.pojedi(pozicija, moguce.get((Slova[unos[0]].value,int(unos[1])-1)),(Slova[unos[0]].value,int(unos[1])-1), "O")
                igrac=0
        
else:
    print("Pogresan unos, pokusajte ponovo")
    exit()

print("gotovo") 
a, b = 0, 0
for red in pozicija:
    for polje in red:
        if polje == "X":
            a+=1
        elif polje =="O":
            b+=1
print("Igrac X: " + str(a))
print("Igrac O: " + str(b))
if a>b:
    print("Igrac X je pobedio")
elif a<b:
    print("Igrac O je pobedio")
else:
    print("Izjednaceno")
