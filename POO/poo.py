class Veiculo:
    # O PyCharm te ajuda a escrever esta parte!
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False # Atributo inicial

    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} está ligado.")

# Crie um segundo arquivo (ou no mesmo) para testar
carro1 = Veiculo("Toyota", "Corolla")
carro1.ligar() # Chamando o método do objeto