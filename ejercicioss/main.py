							#EJERCICIO-01
import random
listanum = []
for indice in range(1,11):
	listanum.append(random.randint(1, 10))
for numero in listanum:
	print(numero," ",numero ** 2," ",numero ** 3)