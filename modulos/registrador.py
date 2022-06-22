from pycep_correios import get_address_from_cep, WebService, exceptions
from modulos.input_padrao import InputPadrao, Menu
from modulos.mensagens import *


class CPF:
    def __init__(self, documento):
        """Classe para validação do numero de CPF.

        Operadores:

        __str__().

        Propriedades:

        @cpf,
        @validar.

        :param documento: str -> numero do documento.
        """
        self.__cpf = documento
        self.__cpf_form = f"{self.__cpf[:3]}.{self.__cpf[3:6]}." \
                          f"{self.__cpf[6:9]}-{self.__cpf[9:]}"

    def __str__(self):
        return self.__cpf_form

    @property
    def cpf(self):
        """Getter da Classe.

        :return: str -> CPF formatado.
        """
        return self.__cpf_form

    @property
    def validar(self):
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


class Documento(CPF):
    def __init__(self, documento: str):
        """Classe para verificação final do documento.

        Propriedade:

        @checar.

        :param documento: str -> número do documento
        """
        super().__init__(documento)
        self.__doc = documento

    @property
    def checar(self):
        """Verifica o tamanho da string passada, e se ela contém apenas números.

        :return: bool -> True | False
        """
        if len(self.__doc) == 11 and self.__doc.isalnum():
            if CPF(self.__doc).validar:
                return True
            else:
                print(msg_registrador_01)
                return False
        else:
            print(msg_registrador_01)


class Endereco:
    def __init__(self, entrada='=> '):
        """Obtém o endereço através do CEP.

        Privado:

        __validar_cep

        Propriedade:

        @endereco

        :param entrada: str -> input usuário.
        """
        self.__end = self.__validar_cep(entrada)
        self.__numero = InputPadrao('Número da residência:\n=> ', int).conteudo
        self.__end_linha_1 = f"{self.__end['logradouro']} nº{self.__numero} | CEP:{self.__end['cep']}"
        self.__end_linha_2 = f"{self.__end['bairro']} - {self.__end['cidade']}/{self.__end['uf']}"

    def __validar_cep(self, entrada):
        """Método privado para validação do número de CEP. Utiliza a API
        pycep_correios para realizar a consulta.

        :param entrada: str -> CEP
        :return: dict -> dados endereço
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

        :return: dict -> dados endereço.
        """
        return {'endereco': self.__end_linha_1, 'bairro': self.__end_linha_2}


class Cliente:
    def __init__(self, dados):
        """

        :param dados:
        """
        self.__nome = dados['nome']
        self.__cpf = dados['cpf']
        self.__endereco = dados['endereco']
        self.__bairro = dados['bairro']

    @property
    def dados_cliente(self):
        return {'nome': self.__nome, 'cpf': self.__cpf,
                'endereco': self.__endereco, 'bairro': self.__bairro}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco


class Conta:
    def __init__(self, dados):
        self.__saldo = float(dados['saldo'])
        self.__credito = float(dados['credito'])
        self.__disponivel = self.__saldo + self.__credito

    @property
    def dados_conta(self):
        return {'saldo': self.__saldo, 'credito': self.__credito,
                'disponivel': self.__saldo + self.__credito}

    @property
    def saldo(self):
        return self.__saldo

    @property
    def credito(self):
        return self.__credito

    @credito.setter
    def credito(self, valor: float):
        self.__credito = valor

    @property
    def disponivel(self):
        return self.__disponivel

    def __validar_saque(self, valor: float):
        return valor <= self.__disponivel

    def sacar(self, valor: float):
        if self.__validar_saque(valor):
            self.__saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor: float):
        self.__saldo += valor


class Registro:
    @property
    def registrar_cliente(self):
        nome = InputPadrao('Nome: ').conteudo
        cpf = InputPadrao('CPF: ').conteudo
        while not Documento(cpf).checar:
            cpf = InputPadrao('CPF: ').conteudo
        endereco = Endereco('Digite o seu CEP: ').endereco
        return {'nome': nome, 'cpf': Documento(cpf).cpf, **endereco}

    @property
    def registrar_conta(self):
        saldo = InputPadrao('Saldo: ', float).conteudo
        if Menu().menu_creditos == 1:
            credito = InputPadrao('Limite: ', float).conteudo
        else:
            credito = 0
        return {'saldo': saldo, 'credito': credito}