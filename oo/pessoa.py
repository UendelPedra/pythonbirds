class Pessoa:
    def __init__(self, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return 'Olá'
if __name__ == '__main__':
    p = Pessoa('Uendel')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)