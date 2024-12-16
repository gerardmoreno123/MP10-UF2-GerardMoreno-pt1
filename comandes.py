from errors import ProducteExistentError, ProducteInexistentError

class Comanda:
    def __init__(self, id):
        self.id = id
        self.productes = {}
        self.estat = "Pendent"

    # Afegir producte a la comanda
    def afegir_producte(self, producte, quantitat=1):
        if producte.nom in self.productes:
            raise ProducteExistentError(f"El producte {producte.nom} ja existeix a la comanda.")
        self.productes[producte.nom] = quantitat

    # Afegir unitats d'un producte a la comanda
    def afegir_unitats(self, producte, quantitat=1):
        if producte.nom not in self.productes:
            raise ProducteInexistentError(f"El producte {producte.nom} no existeix a la comanda.")
        self.productes[producte.nom] += quantitat

    # Consultar resum de la comanda
    def consultar_resum(self):
        return f"Comanda {self.id} [{self.estat}]: " + ", ".join(f"{prod}: {quant}" for prod, quant in self.productes.items())

    # Modificar l'estat de la comanda
    def modificar_estat(self, nou_estat):
        self.estat = nou_estat

    def __str__(self):
        return self.consultar_resum()