"""implementati functia process care primeste o lista 
numita data care contine numere intregi. Functia va trebui sa :
- numere cate cifre pare are fiecare numar 
- calculeze media numerelor fara cifre pare
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

def read(file_name,file_name2):
    lista_return = []
    with open(file_name, 'r') as f:
        for line in f:
            lista_return.append(process([int(x) for x in line.split()]))
    write(file_name2, lista_return)


def write(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            formatted_line = ' '.join(str(x) for x in line)
            f.write(f"{formatted_line}\n")

read('text.txt', 'output.txt')
