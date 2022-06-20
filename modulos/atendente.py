class Cliente:
    def __init__(self, dados=None):
        self.__dados = dados
        self.__nome = self.__dados[0]
        self.__cpf = self.__dados[1]
        self.__endereco = self.__dados[2]

    @property
    def dados(self):
        return self.__dados

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco


class Conta:
    def __init__(self, dados=None):
        self.__dados = dados
        self.__saldo = self.__dados[0]
        self.__credito = self.__dados[1]
        self.__disponivel = self.__dados[2]

    @property
    def dados(self):
        return [self.__saldo, self.__credito, self.__disponivel]

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__credito

    @limite.setter
    def limite(self, valor: float):
        self.__credito = valor

    def validar_saque(self, valor):
        return valor <= self.__disponivel

    def sacar(self, valor):
        if self.validar_saque(valor):
            self.__saldo -= valor
            self.__disponivel = self.__saldo + self.__credito
        else:
            print(f"O valor de R${valor:.2f}, excedeu o seu limite!")

    def depositar(self, valor):
        self.__saldo += valor
        self.__disponivel = self.__saldo + self.__credito