# Passo 1: Plano
# Problema escolhido: calculadora de tarifa de estacionamento por perfil de usuário
# (componente novo, ainda não desenvolvido por mim em atividades anteriores; o contexto
# é o app de estacionamento do campus, mas as regras de preço abaixo são hipóteses
# didáticas desta atividade, não vêm do e-mail do cliente).
#
# Casos a testar (3 variações de comportamento, 2 testes por variação):
#   1. Aluno: R$ 2,00 por hora iniciada, limitado a R$ 10,00 por dia.
#   2. Funcionário: sempre gratuito (R$ 0,00).
#   3. Visitante: R$ 5,00 por hora iniciada, com tolerância de 15 min gratuitos.
#   (+ 1 teste para perfil desconhecido, que deve levantar ValueError.)
#
# Padrão de projeto escolhido: Strategy.
# Por quê: a única coisa que muda entre os casos é a regra de cálculo, selecionada pelo
# perfil. Com Strategy, cada regra vira uma classe própria e um novo perfil entra sem
# alterar a CalculadoraTarifa (aberto/fechado), eliminando a cadeia de if/elif.
#
# Tempo planejado: 20 min para testes (red), 25 min para implementação direta (green),
# 40 min para refatoração com Strategy, 15 min para autoavaliação e ajustes.
# Uso de IA: Claude ajudou a estruturar os casos de teste e a aplicar o padrão Strategy.

import pytest

from tarifa import CalculadoraTarifa


# --- Variação 1: Aluno -------------------------------------------------------
def test_aluno_paga_dois_reais_por_hora_iniciada():
    calc = CalculadoraTarifa()
    assert calc.calcular("aluno", minutos=61) == 4.00  # 2 horas iniciadas


def test_aluno_tem_teto_diario_de_dez_reais():
    calc = CalculadoraTarifa()
    assert calc.calcular("aluno", minutos=600) == 10.00  # 10 h = 20,00 sem teto


# --- Variação 2: Funcionário -------------------------------------------------
def test_funcionario_nao_paga_por_estadia_curta():
    calc = CalculadoraTarifa()
    assert calc.calcular("funcionario", minutos=30) == 0.00


def test_funcionario_nao_paga_por_estadia_longa():
    calc = CalculadoraTarifa()
    assert calc.calcular("funcionario", minutos=600) == 0.00


# --- Variação 3: Visitante ---------------------------------------------------
def test_visitante_tem_tolerancia_de_quinze_minutos():
    calc = CalculadoraTarifa()
    assert calc.calcular("visitante", minutos=15) == 0.00


def test_visitante_paga_cinco_reais_por_hora_iniciada_apos_tolerancia():
    calc = CalculadoraTarifa()
    assert calc.calcular("visitante", minutos=16) == 5.00
    assert calc.calcular("visitante", minutos=121) == 15.00  # 3 horas iniciadas


# --- Perfil inválido ---------------------------------------------------------
def test_perfil_desconhecido_levanta_erro():
    calc = CalculadoraTarifa()
    with pytest.raises(ValueError):
        calc.calcular("fantasma", minutos=60)
