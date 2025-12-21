class Cachorro:
    # 1. Defina o CONSTRUTOR que recebe nome e idade
    def __init__(self, nome, idade): # COLOQUE AQUI OS ATRIBUTOS
                 # Atribua os valores recebidos às propriedades do objeto
        self.nome = nome
        self.__idade = idade

    def latir(self):
        # Faça o print, usando o self.nome
        print(f"{self.nome} diz: Au Au!")

    def ver_idade(self):
        return self.__idade

    def aniversario(self):
        print(f"Parabens {self.nome} fez aniversario")
        self.__idade += 1

# 3. Crie o objeto 'buddy'
#buddy = Cachorro ('buddy',3 )
buddy = Cachorro('Buddy', 3)
print(f'idade inicial de {buddy.nome}: {buddy.ver_idade()}')
buddy.aniversario()
print(f'Nova idade de {buddy.nome}: {buddy.ver_idade()} anos.')
buddy.latir()








'''# 4. Chame o método 'latir' do objeto 'buddy'
# COLOQUE AQUI A CHAMADA DO MÉTODO latir'''
