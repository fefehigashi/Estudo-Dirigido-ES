# Módulo responsável por simular a visualização de vagas (REQ-01)
class GerenciadorVagas:
    def __init__(self):
        self.mapa_vagas = {
            "A1": "Disponível",
            "A2": "Ocupada",
            "B1": "Disponível"
        }

    def listar_vagas_livres(self):
        return {vaga: status for vaga, status in self.mapa_vagas.items() if status == "Disponível"}