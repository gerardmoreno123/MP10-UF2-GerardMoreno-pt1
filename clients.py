class Client:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email
        self.comandes = []

    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    def consultar_comandes(self):
        if not self.comandes:
            return f"El client {self.nom} no té cap comanda."
        return f"Comandes del client {self.nom}: {len(self.comandes)}\n" + "\n".join(str(comanda) for comanda in self.comandes)

