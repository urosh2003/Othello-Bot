import f
import heuristika

def minmax(pozicija, trenutni_igrac, alfa, beta, dubina):
    if dubina == 0:
        return heuristika.dynamic_heuristic_evaluation_function(pozicija)

    pozicije = f.moguce_pozicije(pozicija, trenutni_igrac)
    if pozicije=={}:
        return heuristika.dynamic_heuristic_evaluation_function(pozicija)

    if trenutni_igrac == 0:
        maxRez = -999999999
        for moguca_pozicija in pozicije:
            procena = minmax(f.pojedi(pozicija, pozicije.get(moguca_pozicija),moguca_pozicija, "X"), 1, alfa, beta, dubina-1)
            maxRez = max(maxRez, procena)
            alfa = max(procena, alfa)
            if beta <= alfa:
                break
 
        return maxRez
        

    else:
        minRez = 99999999
        for moguca_pozicija in pozicije:
            procena = minmax(f.pojedi(pozicija, pozicije.get(moguca_pozicija),moguca_pozicija, "O"), 0, alfa, beta, dubina-1)
            minRez = min(minRez, procena)
            beta = min(beta, procena)
            if beta <= alfa:
                break
    
        return minRez
    

    