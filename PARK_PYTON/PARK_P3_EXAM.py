from vehiculos import Vehiculo,Auto,Motosicleta,Camion,auto1
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("        AGENCIA DE VEHICULOS MIXTOS")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("SELECCIONA UNA OPCION : \n")
resp = int(input("1-Adquirir un vehiculo.\n2-Debolver el vehiculo.\n"))
match(resp):
    case(1): 
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("                  VEHICULOS")
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        resp2 = int(input("1-Auto\n2-Motosicleta\n3-Camion\n"))
        match(resp2):
            case(1):
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
                print("                     AUTO")
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
                print(auto1)
            case(2):
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
                print("                  MOTOSICLETA")
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
            case(3):
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
                print("                     CAMION")
                print("+++++++++++++++++++++++++++++++++++++++++++++++")
            case _:
                print("OPCION NO BALIDA")

    case(2):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("           DEVOLUCION DE VEHICULOS")
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("devolucion de vehiculo: \n")
        resp3 = int(input("1-Auto\n2-Motosicleta\n3-Camion\n"))
        match(resp3):
            case(1):
                print("")
            case(2):
                print("")
            case(3):
                print("")
            case _:
                print("OPCION NO VALIDA")
    case _:
        print("OPCION NO VALIDA")