from modulos.entrada import MeuInput


class Menu:
    def __init__(self):
        pass

    @property
    def menu_inicial(self):
        resp = MeuInput('Menu Inicial:\n'
                        '[1] Cadastrar Novo Cliente\n'
                        '[2] Buscar Dados do Cliente\n'
                        '[3] Operações em Conta\n'
                        '[0] Encerrar\n=> ', int, 0, 3).menu_input()
        return resp

    @property
    def menu_creditos(self):
        resp = MeuInput('Deseja definir os créditos do cliente?\n'
                        '[1] Sim\n'
                        '[2] Não\n=> ', int, 1, 2).menu_input()
        return resp

    @property
    def menu_operacoes(self):
        resp = MeuInput('Qual operação deseja realizar?\n'
                        '[1] Sacar\n'
                        '[2] Depositar\n'
                        '[3] Consultar extrato\n'
                        '[4] Novo Limite'
                        '[0] Retornar\n=> ', int, 0, 4).menu_input()
        return resp
