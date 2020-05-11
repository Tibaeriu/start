#   primii pasi in python
#   declararea variabilelor, operatori de asignare
#a = int(input('Introduceti prima variabila:'))
#b = int(input('Introduceti a doua variabila:'))
#print (a+b)
#   problema 1 de matematica
#   Alex are cu 13 ani mai multi decat Ionel
#   Impreuna au 45 de ani
#   Cati ani are fiecare?
a = int(input ('Introduceti diferenta de varsta Alex vs Ionel:'))
b = int(input('Introduceti suma de varsta a celor 2:'))
#   a = varsta_Alex - varsta_Ionel
#   b = varsta_Alex + varsta_Ionel
#   formula pentru Ionel va fi: b - varsta_Alex
#   iar 2*varsta_Alex = a + b
#   asadar varsta_Ionel = b - varsta_Alex
print ('Varsta lui Alex este:', (a + b)/2)
print ('Varsta lui Ionel este:', b - (a + b)/2)
    