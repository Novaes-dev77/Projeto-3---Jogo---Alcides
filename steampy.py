from jogos import Jogo
from filabacklog import FilaBackLog
from pilhasrecentes import PilhasRecentes
from sessaodejogo import SessaoJogo


class SteamPy:
    def __init__(self):
        self.catalogo = []
        self.catalogo_dict = {}
        self.backlog = FilaBackLog()
        self.recentes = PilhasRecentes()
        self.historico = []
        self.tempo_jogado = {}

    def carregar_jogos(self, nome_arquivo):
        try:
            arquivo = open(nome_arquivo, encoding="utf-8")
            linhas = arquivo.readlines()
            arquivo.close()

            for i in range(1, len(linhas)):
                try:
                    linha = linhas[i].strip()
                    dados = linha.split(",")

                    jogo = Jogo(
                        i,
                        dados[1],
                        dados[2],
                        dados[3],
                        dados[4],
                        dados[5],
                        float(dados[6]) if dados[6] else 0,
                        float(dados[7]) if dados[7] else 0,
                        float(dados[8]) if dados[8] else 0,
                        float(dados[9]) if dados[9] else 0,
                        float(dados[10]) if dados[10] else 0,
                        float(dados[11]) if dados[11] else 0,
                        dados[12],
                    )

                    self.catalogo.append(jogo)
                    self.catalogo_dict[jogo.id_jogo] = jogo

                except:
                    continue

            print("Catálogo carregado com sucesso!")

        except:
            print("Erro ao carregar arquivo!")

    def buscar_jogo_por_nome(self, termo):
        for jogo in self.catalogo:
            if termo.lower() in jogo.titulo.lower():
                jogo.exibir()

    def adicionar_ao_backlog(self, id_jogo):
        if id_jogo in self.catalogo_dict:
            self.backlog.enqueue(self.catalogo_dict[id_jogo])
            print("Adicionado ao backlog!")

    def jogar_proximo(self):
        jogo = self.backlog.dequeue()
        if jogo:
            print("Jogando:")
            jogo.exibir()
            self.recentes.push(jogo)
        else:
            print("Backlog vazio!")

    def registrar_sessao(self, id_jogo, tempo):
        if id_jogo not in self.catalogo_dict:
            print("Jogo inválido!")
            return

        jogo = self.catalogo_dict[id_jogo]

        self.tempo_jogado[id_jogo] = self.tempo_jogado.get(id_jogo, 0) + tempo
        total = self.tempo_jogado[id_jogo]

        if total < 2:
            status = "iniciado"
        elif total < 10:
            status = "em andamento"
        elif total < 20:
            status = "muito jogado"
        else:
            status = "concluido"

        sessao = SessaoJogo(jogo, tempo, total, status)
        self.historico.append(sessao)

        self.recentes.push(jogo)

        print("Sessão registrada!")

    def mostrar_historico(self):
        for s in self.historico:
            s.exibir()

    def exibir_dashboard(self):
        print("Total jogos:", len(self.catalogo))
        print("Backlog:", self.backlog.tamanho())
        print("Recentes:", self.recentes.tamanho())
        print("Sessões:", len(self.historico))
        print("Tempo total:", sum(self.tempo_jogado.values()))

    def filtrar_por_genero(self, genero):
        encontrados = 0
        genero = genero.lower().strip()

        for jogo in self.catalogo:
            if jogo.genero and genero in jogo.genero.lower():
                jogo.exibir()
                encontrados += 1

        if encontrados == 0:
            print("Nenhum jogo encontrado para esse gênero.")

    def filtrar_por_console(self, console):
        encontrados = 0
        console = console.lower().strip()

        for jogo in self.catalogo:
            if jogo.console and console in jogo.console.lower():
                jogo.exibir()
                encontrados += 1

        if encontrados == 0:
            print("Nenhum jogo encontrado para esse console.")

    def filtrar_por_nota(self, nota_minima):
        encontrados = 0

        for jogo in self.catalogo:
            if jogo.critic_score >= nota_minima:
                jogo.exibir()
                encontrados += 1

        if encontrados == 0:
            print("Nenhum jogo encontrado com essa nota.")