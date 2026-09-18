# Módulo responsável por simular o acesso rápido sem login constante (REQ-03)
class SistemaAcesso:
    def __init__(self):
        self.cache_autenticacao = True  # Simula que o usuário logou na primeira vez

    def iniciar_aplicativo(self):
        if self.cache_autenticacao:
            return "[SISTEMA] App iniciado rapidamente. Sessão recuperada do cache sem pedir credenciais."
        return "[SISTEMA] Por favor, faça seu login inicial."