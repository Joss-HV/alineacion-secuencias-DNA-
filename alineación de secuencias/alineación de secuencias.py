
with open("fasta.txt", "r") as fasta:
    secuencia1= fasta.readlines()
    cadena1=""
    for i in range(1,len(secuencia1)):
        cadena1 += secuencia1[1]
    cadena1=cadena1.replace("\n", "")
print(cadena1)

with open("fasta2.txt", "r") as fasta2:
    secuencia2 = fasta2.readlines()
    cadena2=""
    for i in range(1,len(secuencia2)):
        cadena2 += secuencia2[1]
    cadena2=cadena2.replace("\n", "")
print(cadena2)

Longitud1 = len(cadena1)
Longitud2 = len(cadena2)

if Longitud1 == Longitud2:
    i = 0
    N = 0
    while (i<Longitud1):
        if (cadena1[i]!=cadena2[i]):

            print(i, cadena1[i], cadena2[i])
            N=N+1
        i = i+1
    print("Hay", N, "diferencias")
else:
    print("No se pueden comparar las cadenas")

