from time import strftime, localtime
from modulos.mensagens import *
from re import search, findall
from os import mkdir


# ----------------------------------------------------------------------------------------------------------------------
#              Classe Relatório
# ----------------------------------------------------------------------------------------------------------------------
class Relatorio:
    def __init__(self, dados: dict):
        """Modela o relatório a ser impresso.

        Construtor:

        __ini__()

        Métodos:

        relatorio_conta()
        relatorio_extrato()

        :param dados: dict - dados para a impressão.
        """
        self.__dados = dados
        self.data = strftime('%d/%m/%Y - %H:%M', localtime())

    def relatorio_conta(self):
        """Modela o relatório do cliente.

        :return: str: relatório
        """
        relatorio = f"Nome: {self.__dados['nome']:<25} | CPF: {self.__dados['cpf']}\n" \
                    f"Logradouro: {self.__dados['endereco']}\n" \
                    f"Bairro: {self.__dados['bairro']}\n" \
                    f"Saldo: R${self.__dados['saldo']:.2f} | Crédito: R${self.__dados['credito']:.2f}\n" \
                    f"Disponível: R${self.__dados['disponivel']:.2f}\n"
        return relatorio

    def relatorio_extrato(self, op, valor):
        """Modela o relatório do extrato.

        :return: str: relatório
        """
        relatorio = f"{op:^25} | {self.data:^25} | {valor:^25}"
        return relatorio


# ----------------------------------------------------------------------------------------------------------------------
#              Classe Gerenciador
# ----------------------------------------------------------------------------------------------------------------------
class Gerenciador(Relatorio):
    def __init__(self, diretorio_cliente: str, dados=None, seletor=None):
        super().__init__(dados)
        self.__diretorio = f'./armazenamento/{diretorio_cliente}'
        self.__arquivo_conta = f'./armazenamento/{diretorio_cliente}/conta.txt'
        self.__arquivo_extrato = f'./armazenamento/{diretorio_cliente}/extrato.txt'
        self.__arquivo = self.__definir_nome_arquivo(seletor)
        try:
            mkdir('./armazenamento/')
        except FileExistsError:
            pass

    def __definir_nome_arquivo(self, seletor):
        if seletor == 'ext':
            return self.__arquivo_extrato
        else:
            return self.__arquivo_conta

    def procurar(self, seletor=None):
        try:
            arquivo_conta = open(self.__definir_nome_arquivo(seletor), 'rt')
            arquivo_conta.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def visualizar(self):
        try:
            arquivo_conta = open(self.__arquivo, 'rt')
            print(arquivo_conta.read())
            arquivo_conta.close()
        except FileNotFoundError:
            return msg_gerenciador_03

    def escrever_extrato(self, op, valor):
        if self.procurar('ext'):
            arquivo_extrato = open(self.__arquivo_extrato, 'at')
            arquivo_extrato.write(f'{super().relatorio_extrato(op, valor)}\n')
            arquivo_extrato.close()
            return msg_gerenciador_02
        else:
            try:
                mkdir(self.__diretorio)
            except FileExistsError:
                pass
            topo = f"{'OPERAÇÃO':^25} | {'DATA':^25} | {'VALOR':^25}"
            linha = "-" * len(topo)
            arquivo_extrato = open(self.__arquivo_extrato, 'wt+')
            arquivo_extrato.write(f"{topo}\n{linha}\n{super().relatorio_extrato(op, valor)}\n")
            arquivo_extrato.close()
        return msg_gerenciador_01

    def escrever_conta(self):
        if self.procurar():
            arquivo_cliente = open(self.__arquivo, 'wt+')
            arquivo_cliente.write(f'{super().relatorio_conta()}')
            arquivo_cliente.close()
            return msg_gerenciador_02
        else:
            try:
                mkdir(self.__diretorio)
            except FileExistsError:
                pass
            arquivo_cliente = open(self.__arquivo, 'wt+')
            arquivo_cliente.write(f'{super().relatorio_conta()}')
            arquivo_cliente.close()
            return msg_gerenciador_01

    def extrair_dados(self):
        dados = dict()
        padrao_cpf = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
        padrao_valor = '[0-9]{1,24}.[0-9]{2}'
        try:
            arquivo = open(self.__arquivo, 'rt')
            conteudo = [user_data.strip() for user_data in arquivo.readlines()]
            dados['nome'] = conteudo[0][conteudo[0].find(':') + 1:conteudo[0].find('|')].strip()
            dados['cpf'] = search(padrao_cpf, conteudo[0]).group().strip()
            dados['endereco'] = conteudo[1][conteudo[1].find(':') + 1:].strip()
            dados['bairro'] = conteudo[2][conteudo[2].find(':') + 1:].strip()
            dados['saldo'] = float(findall(padrao_valor, conteudo[3])[0])
            dados['credito'] = float(findall(padrao_valor, conteudo[3])[1])
            dados['disponivel'] = float(findall(padrao_valor, conteudo[4])[0])
            arquivo.close()
            return dados
        except FileNotFoundError:
            return msg_gerenciador_03