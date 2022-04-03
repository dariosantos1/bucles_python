# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
numero_1 = int(input("Ingrese el primer numero a calcular : \n"))
numero_2 = int(input("Ingrese el segundo numero a calcular : \n"))
simbolo = 0
while simbolo != 7 :
    print ("""
    Indique la operacion a realizar:
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Exponente/Potencia
    6) Fin (Salir)
    """)
    simbolo = int(input())
    if simbolo == 1 :
        print ("Resultado: \n" ,numero_1, "+" ,numero_2, "=", numero_1+numero_2)
    elif simbolo == 2 :
        print ("Resultado: \n" ,numero_1, "-" ,numero_2, "=" , numero_1-numero_2)
    elif simbolo == 3 :
        print ("Resultado: \n" ,numero_1, "*" ,numero_2, "=" , numero_1*numero_2)
    elif simbolo == 4 :
        print ("Resultado: \n" ,numero_1, "/" ,numero_2, "=" , float(numero_1/numero_2))
    elif simbolo == 5 :
        print ("Resultado: \n" ,numero_1, "La potencia" ,numero_2, "=" , numero_1**numero_2)
    elif simbolo == 6 :
        print ("Gracias por usar la calculadora")
        break
    else : 
        print ("Error")





