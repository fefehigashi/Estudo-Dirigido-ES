import math


class CalculadoraTarifa:
    def calcular(self, perfil, minutos):
        horas = math.ceil(minutos / 60)
        if perfil == "aluno":
            return min(horas * 2.00, 10.00)
        elif perfil == "funcionario":
            return 0.00
        elif perfil == "visitante":
            if minutos <= 15:
                return 0.00
            return horas * 5.00
        else:
            raise ValueError(f"Perfil desconhecido: {perfil}")
