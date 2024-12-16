from clients import Client
from comandes import Comanda
from productes import Producte
from errors import  ProducteExistentError, ProducteInexistentError

def test():
    # Crear clients
    anna = Client(1, "Anna", "anna@example.com")
    pere = Client(2, "Pere", "pere@example.com")
    joan = Client(3, "Joan", "joan@example.com")

    # Crear productes
    bicicleta = Producte("bicicleta")
    casc = Producte("casc")
    guants = Producte("guants")
    maillot = Producte("maillot")
    roda = Producte("roda")
    pantalons = Producte("pantalons")
    patinet = Producte("patinet")

    # Crear comandes i afegir-les als clients
    comanda1 = Comanda(101)
    comanda1.afegir_producte(bicicleta)
    comanda1.afegir_producte(casc, 2)
    anna.afegir_comanda(comanda1)

    comanda2 = Comanda(102)
    comanda2.afegir_producte(guants)
    anna.afegir_comanda(comanda2)

    comanda3 = Comanda(103)
    comanda3.afegir_producte(maillot)
    comanda3.afegir_producte(roda, 2)
    pere.afegir_comanda(comanda3)

    comanda4 = Comanda(104)
    comanda4.afegir_producte(guants, 2)
    pere.afegir_comanda(comanda4)

    # Mostrar comandes dels clients
    print("COMANDES DELS CLIENTS")
    print(anna.consultar_comandes())
    print("\n")
    print(pere.consultar_comandes())
    print("\n")
    print(joan.consultar_comandes())

    # Gestionar errors
    try:
        comanda1.afegir_producte(bicicleta)
    except ProducteExistentError as e:
        print(e)

    try:
        comanda1.afegir_unitats(patinet)
    except ProducteInexistentError as e:
        print(e)

    # Modificar comandes
    comanda1.modificar_estat("Enviada")
    comanda1.afegir_unitats(bicicleta)
    comanda1.afegir_unitats(casc, 2)
    comanda1.afegir_producte(pantalons)

    # Mostrar comandes actualitzades
    print("\nCOMANDES DELS CLIENTS")
    print(anna.consultar_comandes())

if __name__ == "__main__":
    test()