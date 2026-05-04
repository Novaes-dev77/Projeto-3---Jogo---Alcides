class SessaoJogo:
    def __init__(self, jogo, tempo, total, status):
        self.jogo = jogo
        self.tempo = tempo
        self.total = total
        self.status = status

    def exibir(self):
        print(f"{self.jogo.titulo} | Sessão: {self.tempo}h | Total: {self.total}h | Status: {self.status}")