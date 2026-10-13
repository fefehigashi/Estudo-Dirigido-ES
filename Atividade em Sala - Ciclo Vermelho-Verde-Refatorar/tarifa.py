# Fase REFACTOR: padrão de projeto STRATEGY.
#
# Participantes (nomeados conforme o domínio):
#   - Strategy (interface):      EstrategiaTarifa     -> define calcular(minutos)
#   - ConcreteStrategy:          TarifaAluno          -> R$ 2,00/hora iniciada, teto diário R$ 10,00
#                                TarifaFuncionario    -> sempre gratuito
#                                TarifaVisitante      -> R$ 5,00/hora iniciada, 15 min de tolerância
#   - Context:                   CalculadoraTarifa    -> escolhe a estratégia pelo perfil e delega o cálculo
#
# O comportamento observável é o mesmo da fase green; só a estrutura mudou.
import math
from abc import ABC, abstractmethod


def _horas_iniciadas(minutos):
    return math.ceil(minutos / 60)


class EstrategiaTarifa(ABC):
    """Strategy: contrato comum a todas as regras de cobrança."""

    @abstractmethod
    def calcular(self, minutos):
        ...


class TarifaAluno(EstrategiaTarifa):
    VALOR_HORA = 2.00
    TETO_DIARIO = 10.00

    def calcular(self, minutos):
        return min(_horas_iniciadas(minutos) * self.VALOR_HORA, self.TETO_DIARIO)


class TarifaFuncionario(EstrategiaTarifa):
    def calcular(self, minutos):
        return 0.00


class TarifaVisitante(EstrategiaTarifa):
    VALOR_HORA = 5.00
    TOLERANCIA_MIN = 15

    def calcular(self, minutos):
        if minutos <= self.TOLERANCIA_MIN:
            return 0.00
        return _horas_iniciadas(minutos) * self.VALOR_HORA


class CalculadoraTarifa:
    """Context: não conhece as regras, apenas escolhe a estratégia do perfil."""

    def __init__(self):
        self._estrategias = {
            "aluno": TarifaAluno(),
            "funcionario": TarifaFuncionario(),
            "visitante": TarifaVisitante(),
        }

    def calcular(self, perfil, minutos):
        try:
            estrategia = self._estrategias[perfil]
        except KeyError:
            raise ValueError(f"Perfil desconhecido: {perfil}") from None
        return estrategia.calcular(minutos)


# Passo 3: Autoavaliação
# Critérios atingidos:
#   (1) Testes em arquivo separado (test_tarifa.py), com 2 testes para cada uma das 3 variações
#       (aluno, funcionário, visitante) + 1 teste de perfil inválido: atingido.
#   (2) Histórico com 3 commits (red, green, refactor) com a fase na mensagem: atingido.
#   (3) Commit red contém só os testes (+ .gitignore) e não a implementação: atingido.
#   (4) Refatoração aplica o padrão Strategy, nomeado em comentário, com participantes
#       nomeados conforme o domínio: atingido.
#   (5) Suíte executa e passa após a refatoração; saída registrada em saida_testes.txt: atingido.
# O que mudou entre green e refatorado: o if/elif único por perfil virou uma hierarquia
# (EstrategiaTarifa + 3 classes concretas) e CalculadoraTarifa passou a só escolher a
# estratégia num dicionário. Para um novo perfil basta criar uma classe e registrá-la, sem
# mexer nas regras existentes.
# Parte que deu mais trabalho: manter exatamente o mesmo comportamento no perfil inválido
# (ValueError) e decidir onde ficam as constantes (valor/hora, teto, tolerância), que foram
# para dentro de cada estratégia. As regras de preço são hipóteses minhas, não do cliente.
# IA: Claude ajudou a levantar os casos de teste e a estruturar o Strategy, poupando tempo;
# atrapalhou apenas por sugerir inicialmente mais perfis do que o necessário, que descartei.
