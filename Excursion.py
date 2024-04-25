import random


titulo = ("Bienvenido a la excursión maldita. Resulta que tienes apenas 12 años y te vas de excursión a un desierto con la clase de tu escuela.\n"
         "Hay una tormenta de arena bastante fuerte y apenas hay algo de visibilidad.\n")
print(titulo)
print("-----------")
opcion =str("")

print("Te distraes observando una planta y para cuando te das cuenta, te has quedado muy atrás.")

opcion = input ("A: Te quedas quieto | B: Echas a correr | C: Te pones a gritar: ")
if opcion == "A":
     print("mueres en muy poco tiempo debido a las altas temperaturas y el sol intenso, FIN.")
elif opcion == "B":
     print("Corres hacia adelante hasta que ves lo que parece ser una sombra.")
     
     opcion = input (" A: Vas hacia la sombra | B: Vuelves hacia atrás: ")

     if opcion == "A":
        print("Se trata de una pantera y te mata, FIN.")
     elif opcion == "B":
        print("Vuelves a zona segura y empiezas a ver huellas de tu grupo, aunque escuchas que algo te persigue y tienes mucho miedo. Ves una roca afilada")
        
        opcion = input ("A: Coges la roca | B: La ignoras: ")
          
        roca_afilada = False
        if opcion == "A": 
            roca_afilada = True
        elif opcion =="B": 
            roca_afilada = False
              
        numero_random = random.randint(1, 10)
              
        print("Sigues las huellas y llegas hasta una puerta de piedra con un enigma y unos dibujos. \n"
                "Crees entender que, aunque parezca de locos, hay que responder mal apropósito, pues es una trampa. \n"
                "El enigma dice algo así como (8 * {}).".format(numero_random))
          
        opcion = int(input("¿Cual es la respuesta?: "))
        if opcion == 8 * numero_random:
               print ("la puerta explota y mueres, FIN")
        else:
              print ("la puerta se abre y decides adentrartre en la cueva.")
        
        print("Escuchas ruidos muy extraños detrás de ti, por lo que te giras rápidamente, descubres que es una persona corriendo hacia ti y decides defenderte:")

        opcion = input("A: Ignorarlo | B: Defenderte")
        
        if opcion == "A":
             print("Se acerca y te dice que no te asustes, que viene a ayudarte. Es tu profesor y te rescata, FIN.")
        elif opcion == "B" and roca_afilada:
            print("Te giras y lanzas la piedra que habías cogido antes. Verás que acabas de asesinar a tu profesor que venía a rescatarte, FIN")

elif opcion == "C":
     print("Empiezas a oir gritos de alguien que te responde")

     opcion = input("A: Lo ignoras | B: Te diriges hacia donde provienen los gritos ")

     if opcion == "A":
          print("Sigues solo, desorientado y perdido. Acabas muriendo de deshidratación, FIN.")
     elif opcion == "B":
          print("Te da la sensación de que es alguien conocido, por lo que vas corriendo.")

          print("De camino hacia la voz, te tropiezas con una piedra muy afilada y caes.")

          opcion = input ("A: Coges la piedra y sigues tu camino | B: Te levantas y sigues tu camino: ")
          
          roca_afilada = False

          if opcion == "A": 
               roca_afilada = True
          elif opcion =="B": 
               roca_afilada = False
               
               numero_random = random.randint(1, 10)
               
               print("Continuas hasta llegar a un oasis y en el agua ves que hay unas flores flotando y un enigma, al que \n"
                     "sin ningún motivo aparente, te decides a resolver. Las flores parecen simular una resta \n"
                     "Pone (15 * {}." ,format(numero_random), "Pero debajo hay un cartel que pone que solo se aceptan respuestas incorrectas: ")
               
               opcion = int(input("¿Cual es la respuesta?: "))
               if opcion == 15 * numero_random:
                    print ("el oasis se transforma en un agujero negro que te absorbe y mueres, FIN.")
               else:
                    print ("Te muestra una flecha en el agua hacia donde debes continuar tu camino.")

                    print("Escuchas ruidos muy extraños detrás de ti, por lo que te giras rápidamente, descubres que es una persona corriendo hacia ti y decides defenderte:")
                    
                    opcion = input("A: Ignorarlo | B: Defenderte")
                    
                    if opcion == "A":
                        print("Se acerca y te dice que no te asustes, que viene a ayudarte. Es tu profesor y te rescata, FIN.")
                    elif opcion == "B" and roca_afilada:
                        print("Te giras y lanzas la piedra que habías cogido antes. Verás que acabas de asesinar a tu profesor que venía a rescatarte, FIN")