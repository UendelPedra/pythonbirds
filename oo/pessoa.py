class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'Olá'
if __name__ == '__main__':
    esther = Pessoa(nome='Esther')
    marly = Pessoa(nome='Marly')
    uendel = Pessoa(esther, marly, nome='uendel')
    print(uendel.cumprimentar())
    print(uendel.nome)
    print(uendel.idade)
    for filho in uendel.filhos:
        print(filho.nome)
    del uendel.filhos
    uendel.olhos = 1
    print(uendel.__dict__)
    print(esther.__dict__)
    print(Pessoa.olhos)
    print(uendel.olhos)
    print(esther.olhos)
    print(id(Pessoa.olhos), id(uendel.olhos), id(esther.olhos))