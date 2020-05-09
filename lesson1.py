#   Operatori de asignare
a = 77
b = 20.89
a = a + b #a +=b
a = a - b #a -=b
#   print (a)

#   ==== String ==========
nume = 'John'
nume = "John"
nume = """John"""
#   cu ce ghilimele incep, asa trebuie sa si termin

#   date mutabile si imutabile
#   stringul este data imutabila

#   in programare primul element dintr-o variabila este pe pozitia zero si nu pe pozitia 1
#   0 = J, 1 = o, 2 = h, 3 = n
#   Index -1 = ultimul element din string
localitate  = 'Bucuresti'
rezultat = nume + localitate
print (rezultat)
#   stringurile pot fi concatenate cu semnul +
#   stringurile pot fi *
rezultat = rezultat * 3
print (rezultat)

#   string slicing (taiere de elemente):
primul_ch = rezultat[0]
print(primul_ch)
second_ch = rezultat[1]
print(second_ch)
last_ch = rezultat[-1]
print(last_ch)
ante_ch = rezultat[-2]
print(ante_ch)
#   invers, de la dreapta la stanga, incepem de la -1, apoi -2, -3 samd
#   daca dam numere prea mari > error, out of range

rezultat = 'PYTHON'
print(rezultat[0:3])
#   apare doar PYT (adica elementele 012 fara 3)
print(rezultat[2:5])
#   la final insa print(rezultat) va fi PYTHON deoarece stringul este imutabil

#   metoda built-in len
nr_elemente = len(rezultat)
print(nr_elemente)
print('Stringul', rezultat, 'are', nr_elemente, 'elemente')

#   Captarea inputului

answer = input('introduceti varsta:')
print(answer)
print(type(answer))
# ca sa aflam tipul de variabila
#   problema
varsta_elev1 = int(input('introdu varsta:'))
varsta_elev2 = varsta_elev1 - 4
print(varsta_elev2)
#   cu int de la integer convertim string in numere

#   Convertire string in integer > str ()
#   Dar cum convertim un integer in string > int()

a = 10; print(type(a))
a = str(a); print(type(a))

#   %s = string; %d = integer
#   string.format()
#   F-strings

#   print(type(info))

#   Built-in methods: string.method()
name = 'Alex'
#help(str)
name = "skdncaksncndsacsa. dscdsac.da.dscsadcd"
print(name.count(a))
#   returneaza de cate ori a apare in interiorul lui name
print(name.capitalize())
print(name.lower())
home = 'ilfov'
print(home.upper())
print(home.index('f'))

import math
math.pi

#   IF / ELIF / ELSE
variabila = ''

print(bool(variabila))

if None:
    print ('TEXT!!!!')

#   False  = variabila empty, 0
#   True = variabila non-empty, 1

#   Operatori booleani:
#   1. == : face comparatie
print(5 == 5)
print(10>20)
print(7 != 8)
print(10>=9)
print(2<5)
print (2<5 and 2>=2)
#   false cu false ne da TRUE
#   false cu true ne da FALSE
#   true cu true ne da TRUE
print(1==1 or 2==2)
#   T or T - > True, T or F -> T, F or F -> F

#   in / not in : t/F : testeaza apartenenta unui element intr-o secventa
info = 'I live in Bucharest'
print('galati' not in info)
#   is/ is not: T/F: testeaza object identitiy (testeaza daca 2 variabile pointeaza catre acelasi obiect valoare)
a = 100
b = 100
print('Operatorul "is":', b is a)

#sapt urmatoare while if elsif else samd...