# Módulo responsável por aplicar a restrição de vagas da biblioteca (REQ-02)
class ValidadorEstacionamento:
    def __init__(self):
        self.vagas_funcionarios = ["BIB-1", "BIB-2"]

    def tentar_estacionar(self, id_vaga, perfil_usuario):
        if id_vaga in self.vagas_funcionarios and perfil_usuario == "Aluno":
            return f"[ALERTA] Acesso Negado: A vaga {id_vaga} é exclusiva para Funcionários."
        return f"[SUCESSO] Veículo estacionado na vaga {id_vaga}."