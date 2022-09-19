import random
import time


iniciar_trivia = True
intentos = 0

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[39m'

print ("Bienvenido a mi trivia sobre motos")
print ("Pondremos a prueba tus conocimientos")
nombre = input("Ingresa tu nombre: ")

while iniciar_trivia == True:
  intentos += 1
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  
  puntaje = random.randint(0, 1000)
  print("Comenzarás con ", puntaje, "puntos")
  
  for tiempo in range(5, 0, -1):
    print(tiempo)
    time.sleep(1)
  
  print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
  
  # Pregunta 1
  print (GREEN+"1) ¿Qué moto es mejor para off road?"+RESET)
  print ("a) Custom")
  print ("b) Trail")
  print ("c) Cruiser")
  print ("d) Cafe racer")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d", "z"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    puntaje -= random.randint(5, 50)
    print(RED+"Incorrecto!", nombre, "La Custom es una moto muy personalizada."+RESET)
  elif respuesta_1 == "c":
    puntaje -= random.randint(5, 50)
    print("Incorrecto!", nombre, "La Cruiser es una moto para distancias largas en carretera.")
  elif respuesta_1 == "d":
    puntaje -= random.randint(5, 50)
    print("Incorrecto!", nombre, "La Cafe racer es una moto ligera, solo con lo necesario para correr.")
  elif respuesta_1 == "z":
    puntaje += 1000
    print("Vaya sorpresa!", nombre, "Diste con la respuesta secreta, recibes 100 puntos")
  else:
    puntaje += 100
    print("Muy bien", nombre, "!")
  
  print(YELLOW+nombre, "ahora tienes", puntaje, "puntos"+RESET)
  time.sleep(2)
  
  # Pregunta 2
  print (GREEN+"2) ¿Qué estilo de moto es la Honda cb190r?"+RESET)
  print ("a) Trail")
  print ("b) Scooter")
  print ("c) Naked")
  print ("d) Scrambler")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d", "y"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "a":
    puntaje -= random.randint(5, 50)
    print("Incorrecto!", nombre, "Las Trail son para salirse de la ruta.")
  elif respuesta_2 == "b":
    puntaje -= random.randint(5, 50)
    print("Incorrecto!", nombre, "Las Scooter son motos automaticas.")
  elif respuesta_2 == "d":
    puntaje -= random.randint(5, 50)
    print("Incorrecto!", nombre, "Las Scrambler combinan el estilo viejo y moderno.")
  elif respuesta_2 == "y":
    puntaje += 1000
    print("Vaya sorpresa!", nombre, "Diste con la respuesta secreta, recibes 100 puntos")
  else:
    puntaje += 100
    print("Muy bien", nombre, "!")
  
  print(YELLOW+nombre, "ahora tienes", puntaje, "puntos"+RESET)
  time.sleep(2)
  
  # Pregunta 3
  print (GREEN+"3) ¿Qué moto es del estilo Cruiser?"+RESET)
  print ("a) Suzuki Gixxer 150 SF")
  print ("b) Pulsar Ns 200")
  print ("c) Hero Xpulse")
  print ("d) Suzuki intruder")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d", "x"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    puntaje = puntaje / 2
    print("Incorrecto!", nombre, "Suzuki Gixxer 150 SF es una deportiva de baja cilindrada.")
  elif respuesta_3 == "b":
    puntaje = puntaje - 5
    print("Incorrecto!", nombre, "Pulsar Ns 200 es una moto estilo Naked.")
  elif respuesta_3 == "c":
    puntaje = puntaje - int(input("Ingresa un numero del 1 al 100 (Solo nuemeros plis): "))
    print("Incorrecto!", nombre, "La Hero Xpulse es una moto Trail.")
  elif respuesta_3 == "x":
    puntaje += 1000
    print("Vaya sorpresa!", nombre, "Diste con la respuesta secreta, recibes 100 puntos")
  else:
    puntaje = puntaje * 5
    print(YELLOW+"Muy bien", nombre, "!"+RESET)
  
  print(YELLOW+nombre, "ahora tienes", puntaje, "puntos"+RESET)
  
  for tiempo in range(5, 0, -1):
    print(tiempo)
    time.sleep(1)
  
  puntaje += random.randint(0, 1000)
  
  print (BLUE+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False