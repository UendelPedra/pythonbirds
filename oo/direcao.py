class Direcao:
    direcoes = {1: 'Norte', 2: 'Leste', 3: 'Sul', 4: 'Oeste'}

    def __init__(self, direcao=1):
        self.direcao = direcao
        self.valor = self.direcoes[direcao]

    def gira_direita(self):
        self.direcao += 1
        if self.direcao > 4:
            self.direcao = 1
        self.valor = self.direcoes[self.direcao]
    def gira_esqerda(self):
        self.direcao = self.direcao
        if self.direcao < 1:
            self.direcao = 4
        self.valor = self.direcoes[self.direcao]