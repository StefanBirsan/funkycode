"""implementati functia process care primeste o lista 
numita data care contine numere intregi. Functia va trebui sa :
- numere cate cifre pare are fiecare numar 
- calculeze media numerelor fara cifre pare

functia va returna o lista care contine numarul de cifre pare 
corespunzator fiecarui numar din lista de intrare , iar la finalul 
ei se va adauga media M , daca nu exista numere fara cifre pare 
atunci M = 0 
"""

def process(data):
    lista_return = []
    numar_cifre_pare = 0
    suma_numere_fara_cifre_pare = 0
    numar_numere_fara_cifre_pare = 0
    for numar in data:
        numar_cifre_pare = 0
        for cifra in str(numar):
            if int(cifra) % 2 == 0:
                numar_cifre_pare += 1
        lista_return.append(numar_cifre_pare)
        if numar_cifre_pare == 0:
            numar_numere_fara_cifre_pare += 1
            suma_numere_fara_cifre_pare += numar
    if numar_numere_fara_cifre_pare != 0:
        media = int(suma_numere_fara_cifre_pare / numar_numere_fara_cifre_pare)
        lista_return.append(media)
    else:
        media = 0
        lista_return.append(media)
    return lista_return

"""implementati functia read care primeste ca parametru numele unui fisier 
de intrare care se gasesc numere intregi , pe mai multe linii.
functia va apela functia process pentru a procesa fiecare linie si 
va returna o lista care contine listele corespunzatoare 
fiecarei linii"""

def read(file_name,file_name2):
    lista_return = []
    with open(file_name, 'r') as f:
        for line in f:
            lista_return.append(process([int(x) for x in line.split()]))
    write(file_name2, lista_return)


"""implementati functia write care primeste ca parametru numele unui 
fisier de iesire si un parametru data , in care se gaseste lista de liste generata . functia va scrie in fisier fiecare lista de numere 
pe cate o linie"""

def write(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            f.write(' '.join(str(x) for x in line) + '\n')

read('text.txt', 'output.txt')
