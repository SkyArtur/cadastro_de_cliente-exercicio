from pycep_correios import get_address_from_cep, WebService

from modulos.input_padrao import InputPadrao, Menu
from modulos.mensagens import *


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe CPF
# ----------------------------------------------------------------------------------------------------------------------
class CPF:
    def __init__(self, documento):
        """Classe para validação do numero de CPF.

        Constructors:
            - __init__()

        Operators:
            - __str__()

        Properties:
            - cpf
            - validar

        :param documento: str(xxxxxxxxxxx).
        """
        self.__cpf = documento
        self.__cpf_form = f"{self.__cpf[:3]}.{self.__cpf[3:6]}." \
                          f"{self.__cpf[6:9]}-{self.__cpf[9:]}"

    def __str__(self):
        return self.__cpf_form

    @property
    def cpf(self):
        """Getter da Classe.

        :return: str(000.000.000-00).
        """
        return self.__cpf_form

    @property
    def validar(self):
        """Algoritmo para validação de número de CPF.

        :return: bool(True | False)
        """
        digito_1, digito_2 = 0, 0
        for i, j in enumerate(range(10, 1, -1)):
            digito_1 += int(self.__cpf[i]) * j
        digito_1 = 11 - (digito_1 % 11)
        digito_1 = 0 if digito_1 > 9 else digito_1
        for i, j in enumerate(range(11, 1, -1)):
            digito_2 += int(self.__cpf[i]) * j
        digito_2 = 11 - (digito_2 % 11)
        digito_2 = 0 if digito_2 > 9 else digito_2
        if f"{digito_1}{digito_2}" in self.__cpf:
            return True
        else:
            return False


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe Documento
# ----------------------------------------------------------------------------------------------------------------------
class Documento(CPF):
    def __init__(self, documento: str):
        """Classe para verificação final do documento.

        Constructors:
            - __init__()

        Properties:
            - checar

        :param documento: str(xxxxxxxxxxx).
        """
        super().__init__(documento)
        self.__doc = documento

    @property
    def checar(self):
        """Verifica o tamanho da string passada, e se ela contém apenas números.

        :return: bool(True | False)
        """
        if len(self.__doc) == 11 and self.__doc.isalnum():
            if CPF(self.__doc).validar:
                return True
            else:
                print(msg_registrador_01)
                return False
        else:
            print(msg_registrador_01)


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe Endereco
# ----------------------------------------------------------------------------------------------------------------------
class Endereco:
    def __init__(self, entrada='=> '):
        """Obtém o endereço através do CEP.

        Constructors:
            - __init__()

        Privates:
            - __validar_cep

        Properties:
            - endereco

        :param entrada: input('texto').
        """
        self.__end = self.__validar_cep(entrada)
        self.__numero = InputPadrao('Número da residência:\n=> ', int).conteudo
        self.__end_linha_1 = f"{self.__end['logradouro']} nº{self.__numero} | CEP:{self.__end['cep']}"
        self.__end_linha_2 = f"{self.__end['bairro']} - {self.__end['cidade']}/{self.__end['uf']}"

    def __validar_cep(self, entrada):
        """Método privado para validação do número de CEP. Utiliza a API
        pycep_correios para realizar a consulta.

        :param entrada: str -> CEP
        :return: dict(pycep_correios())
        """
        while True:
            self.__cep = InputPadrao(entrada).cep_input()
            try:
                self.__cep = get_address_from_cep(self.__cep, webservice=WebService.VIACEP)
            except:
                print(msg_registrador_02)
                continue
            else:
                print(msg_registrador_03)
                return self.__cep

    @property
    def endereco(self):
        """Getter da classe.

        :return: dict('endereco': str, 'bairro': str).
        """
        return {'endereco': self.__end_linha_1, 'bairro': self.__end_linha_2}


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe Cliente
# ----------------------------------------------------------------------------------------------------------------------
class Cliente:
    def __init__(self, dados: dict):
        """Instância o objeto Cliente.

        Constructors:
            - __init__()

        Operators:
            - __str__()

        Properties:
            - dados_cliente
            - cpf


        :param dados: dict('nome': str, 'cpf': str, 'endereco': str, 'bairro': str)
        """
        self.__nome = dados['nome']
        self.__cpf = dados['cpf']
        self.__endereco = dados['endereco']
        self.__bairro = dados['bairro']

    @property
    def dados_cliente(self):
        """Getter da classe

        :return: dict('nome': str, 'cpf': str, 'endereco': str, 'bairro': str)
        """
        return {'nome': self.__nome, 'cpf': self.__cpf,
                'endereco': self.__endereco, 'bairro': self.__bairro}

    def __str__(self):
        return self.__cpf

    @property
    def cpf(self):
        """Getter da classe

        :return: str(xxx.xxx.xxx-xx)
        """
        return self.__cpf


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe Conta
# ----------------------------------------------------------------------------------------------------------------------
class Conta:
    def __init__(self, dados: dict):
        """Instância o objeto Conta

        Constructors:
            - __init__()

        Privates:
            - __validar_saque()

        Methods:
            - sacar
            - depositar

        Properties:
            - dados_conta
            - saldo
            - credito
            - disponivel

        :param dados: dict('saldo': float, 'credito': float)
        """
        self.__saldo = float(dados['saldo'])
        self.__credito = float(dados['credito'])
        self.__disponivel = self.__saldo + self.__credito

    def __validar_saque(self, valor: float):
        """Verifica se há valor disponivel para saque.

        :param valor: float(0.0)
        :return: bool(True | False)
        """
        return valor <= self.__saldo + self.__credito

    def sacar(self, valor: float):
        """Decrementa valor de entrada em atributo saldo.

        :param valor: float(0.0)
        :return: bool(True | False)
        """
        if self.__validar_saque(valor):
            self.__saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor: float):
        """Incrementa valor em atributo saldo.

        :param valor: float(0.0)
        """
        self.__saldo += valor

    @property
    def dados_conta(self):
        """Getter da classe.

        :return:dict('saldo': float: 'credito': float, 'disponivel': float)
        """
        return {'saldo': self.__saldo, 'credito': self.__credito,
                'disponivel': self.__saldo + self.__credito}

    @property
    def saldo(self):
        """Getter da classe

        :return: float(saldo)
        """
        return self.__saldo

    @property
    def credito(self):
        """Getter da classe.

        :return: float(credito)
        """
        return self.__credito

    @credito.setter
    def credito(self, valor: float):
        """Setter da classe.

        :param valor: float(0.0)
        """
        self.__credito = valor

    @property
    def disponivel(self):
        """Getter da classe.

        :return: float(0.0)
        """
        return self.__disponivel


# ----------------------------------------------------------------------------------------------------------------------
#                       Classe Registro
# ----------------------------------------------------------------------------------------------------------------------
class Registro:
    """Classe que realiza o registro da conta.

    Properties:
        - registrar_cliente
        - registrar_conta
    """

    @property
    def registrar_cliente(self):
        """Processa o registro do cliente.

        :return: dict('nome': str, 'cpf': str, 'endereco': str)
        """
        nome = InputPadrao('Nome: ').conteudo
        cpf = InputPadrao('CPF: ').conteudo
        while not Documento(cpf).checar:
            cpf = InputPadrao('CPF: ').conteudo
        endereco = Endereco('Digite o seu CEP: ').endereco
        return {'nome': nome, 'cpf': Documento(cpf).cpf, **endereco}

    @property
    def registrar_conta(self):
        """Processa o registro do cliente.

        :return: dict('saldo': float, 'credito': float)
        """
        saldo = InputPadrao('Saldo: ', float).conteudo
        if Menu().menu_creditos == 1:
            credito = InputPadrao('Limite: ', float).conteudo
        else:
            credito = 0
        return {'saldo': saldo, 'credito': credito}
