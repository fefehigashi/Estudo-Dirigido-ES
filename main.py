# Passo 1: Plano
# Requisitos selecionados da especificação: REQ-01 (Vagas), REQ-02 (Restrição Funcionários), REQ-03 (Acesso Rápido)
# Ordem de implementação: 1º Acesso Rápido (simples), 2º Visualização de vagas (médio), 3º Restrição (médio)
# Tempo estimado: 15 minutos por módulo.
# Uso de IA: Gemini ajudou a estruturar o esqueleto das classes e a formatação das saídas no terminal.

from req01_vagas import GerenciadorVagas
from req02_restricao import ValidadorEstacionamento
from req03_acesso import SistemaAcesso

def iniciar_prototipo():
    print("="*40)
    print("   PROTÓTIPO - ESTACIONAMENTO CAMPUS")
    print("="*40)

    # Execução do REQ-03
    print("\n--- Teste REQ-03: Acesso Rápido ---")
    acesso = SistemaAcesso()
    print(acesso.iniciar_aplicativo())

    # Execução do REQ-01
    print("\n--- Teste REQ-01: Vagas em Tempo Real ---")
    vagas = GerenciadorVagas()
    livres = vagas.listar_vagas_livres()
    print("Vagas Atualmente Livres:")
    for vaga in livres:
        print(f" -> {vaga}")

    # Execução do REQ-02
    print("\n--- Teste REQ-02: Restrição da Biblioteca ---")
    validador = ValidadorEstacionamento()
    print(validador.tentar_estacionar("A1", "Aluno"))
    print(validador.tentar_estacionar("BIB-1", "Aluno"))
    print(validador.tentar_estacionar("BIB-2", "Funcionario"))

if __name__ == "__main__":
    iniciar_prototipo()

# Passo 3: Autoavaliação
# Critérios atingidos: Os 3 requisitos foram implementados (1), existe separação correta de módulos/arquivos para cada regra (2), o main atua como entry point único que não exige edição para rodar (3) e a saída comprova os comportamentos no terminal (6).
# Maior dificuldade na tradução em código: Decidir como passar o perfil do usuário para o REQ-02 de forma fluida já que o sistema (REQ-03) pulou o login obrigatório. Resolvido passando o argumento estaticamente nos testes no main.
# IA: Gerou o código base com rapidez de forma que apenas ajustes finos nas regras de negócio fossem necessários.