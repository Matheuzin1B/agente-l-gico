class AgenteLogico:
    def __init__(self):
        # Inicializando o estado do ambiente
        self.luz_ligada = False  # A luz começa desligada
        self.escuro = False  # Começa não escuro
        self.pessoa_na_sala = False  # Não há ninguém na sala inicialmente

    def atualizar_estado(self, escuro, pessoa_na_sala):
        # Atualiza os estados de ambiente
        self.escuro = escuro
        self.pessoa_na_sala = pessoa_na_sala

    def decidir_acao(self):
        # Regra 1: Se está escuro e há uma pessoa na sala, ligar a luz
        if self.escuro and self.pessoa_na_sala:
            self.ligar_luz()
        # Regra 2: Se está claro, desligar a luz
        elif not self.escuro:
            self.desligar_luz()

    def ligar_luz(self):
        if not self.luz_ligada:
            self.luz_ligada = True
            print("Luz ligada!")
        else:
            print("A luz já está ligada.")

    def desligar_luz(self):
        if self.luz_ligada:
            self.luz_ligada = False
            print("Luz desligada!")
        else:
            print("A luz já está desligada.")


# Exemplo de uso
agente = AgenteLogico()

# Caso 1: Está escuro e há uma pessoa na sala
agente.atualizar_estado(escuro=True, pessoa_na_sala=True)
agente.decidir_acao()  # Espera-se que a luz seja ligada

# Caso 2: Está claro e não há ninguém na sala
agente.atualizar_estado(escuro=False, pessoa_na_sala=False)
agente.decidir_acao()  # Espera-se que a luz seja desligada
