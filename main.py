import time

puntaje = 0

iniciar_trivia = True  # Iniciamos la variable en True

intentos = 0  

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[39m'

print ("Bienvenido(a) a mi trivia sobre el Perú")
print ("¡Pongamos a prueba tus conocimientos!")
print("Tienes", puntaje, "puntos")


nombre = input("\n Antes de ello, dime, ¿Cuál es tu nombre?: ")

print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta, cada respuesta correcta sumará 3 puntos y por cada incorrecta se restará 1:\n")

# Pregunta 1
print (GREEN+"1) ¿Es la ciudad más grande del planeta sin acceso por carretera?"+RESET)
print ("a) Ucayali")
print ("b) Iquitos")
print ("c) Amazonas")
print ("d) La Oroya")

respuesta_1 = input("\nTu respuesta: ").lower()

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)

# Verificamos su respuesta
if respuesta_1 == "b":
  puntaje += 3
  print(BLUE+"Excelente", nombre, "!"+RESET)
else:
  print(RED+"Incorrecto", nombre, "!"+RESET)
  puntaje = puntaje -1
time.sleep(2)

# Pregunta 2
print (GREEN+"\n1) ¿Cuál es considerada la ciuadad más alta del mundo?"+RESET)
print ("a) Puno")
print ("b) Cerro de Pasco")
print ("c) Huaraz")
print ("d) La Rinconada")

respuesta_2 = input("\nTu respuesta: ").lower()

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)

# Verificamos su respuesta
if respuesta_2 == "a":
  print (RED+"Incorrecto!", nombre, "Puno es uno de los 24 departamentos del Perú")
  puntaje = puntaje -1
elif respuesta_2 == "b":
  print (RED+"Incorrecto!", nombre, "Aunque se encuentra a 4380 m no es la ciudad más alta"+RESET)
  puntaje = puntaje -1
elif respuesta_2 == "c":
  print (RED+"Incorrecto!", nombre, "Huaraz se encuentra a solo 3052 msnm, pero hay otra a 5100 msnm"+RESET)
  puntaje = puntaje -1
else:
  puntaje += 3
  print (BLUE+"Muy bien", nombre, "!, La Rinconada se encuentra a nada menos que 5100 msnm"+RESET)

  # Pregunta 3
print (YELLOW+"\n1) Pregunta comodín (puedes ganar 5 puntos): ¿Cuál es el ave nacional?"+RESET)
print ("a) El gallinazo")
print ("b) La paloma")
print ("c) El gallito de las rocas")
print ("d) El cóndor andino")

respuesta_3 = input("\nTu respuesta: ").lower()

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)

# Verificamos su respuesta
if respuesta_3 == "a":
  print (RED+"Nooo!", nombre, ":("+RESET)
  puntaje = puntaje -1
elif respuesta_3 == "b":
  print (RED+"Oops!", nombre, "Esta no es la respuesta correcta"+RESET)
  puntaje = puntaje -1
elif respuesta_3 == "d":
  print (RED+"Incorrecto!", nombre, "El cóndor andino no es el ave nacional"+RESET)
  puntaje = puntaje -1
else:
  puntaje += 5
  print (BLUE+"Perfecto", nombre, "!, se encuentra en la región andino-amazónica del noroeste de américa del Sur"+RESET)

print ("Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")