# ---------------------------------------------------------------------------------------1-----
n1 = input("Dime el primer número: ")
n2 = input("Dime el segundo número: ")
res = int(n1) + int(n2)
print("La suma de ambos es ", res)
# ---------------------------------------------------------------------------------------2-----
import random

secret_number = random.randint(1, 10)
res = int(input("Intenta adivinar el número del 1 al 10: "))
while(res != secret_number):
    res = int(input("Incorrecto. Intenta adivinar el número del 1 al 10: "))
print("El número correcto era", secret_number, "!!")
# ---------------------------------------------------------------------------------------3-----
n1 = input("Dime el primer número: ")
n2 = input("Dime el segundo número: ")
op = input("Dime el operador que quieres usar: ")
if (op == "+"):
    res = int(n1) + int(n2)
elif (op == "-"):
    res = int(n1) - int(n2)
elif (op == "*"):
    res = int(n1) * int(n2)
elif (op == "/"):
    res = int(n1) / int(n2)
else:
    res = "ERROR"
print("El resultado es", res)
# ---------------------------------------------------------------------------------------4-----
nombre = "Sara"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años")