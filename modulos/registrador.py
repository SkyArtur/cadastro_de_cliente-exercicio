from modulos.entrada import MeuInput, Menu


class Registro:
    def __init__(self):
        pass

    @property
    def registrar_cliente(self):
        nome = MeuInput('Nome: ').conteudo
        cpf = MeuInput('CPF: ').conteudo
        while not Documento(cpf).checar:
            cpf = MeuInput('CPF: ').conteudo
        endereco = MeuInput('Endereço: ').conteudo
        return [nome, Documento(cpf).cpf, endereco]

    @property
    def registrar_conta(self):
        saldo = MeuInput('Saldo: ', float).conteudo
        menu = Menu().menu_creditos
        if menu == 1:
            credito = MeuInput('Limite: ', float).conteudo
        else:
            credito = 250
        disponivel = saldo + credito
        return [saldo, credito, disponivel]


class RegistroCliente(Registro):
    def __init__(self):
        super().__init__()
        self._user = super().registrar_cliente

    @property
    def cliente(self):
        return self._user


class RegistroConta(Registro):
    def __init__(self):
        super().__init__()
        self._account = super().registrar_conta

    @property
    def conta(self):
        return self._account


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
    def credito(self):
        return self.__credito

    @credito.setter
    def credito(self, valor: float):
        self.__credito = valor
        self.__disponivel = self.__saldo + self.__credito

    def validar_saque(self, valor):
        return valor <= self.__disponivel

    def sacar(self, valor):
        if self.validar_saque(valor):
            self.__saldo -= valor
            self.__disponivel = self.__saldo + self.__credito
        else:
            return False

    def depositar(self, valor):
        self.__saldo += valor
        self.__disponivel = self.__saldo + self.__credito


class CPF:
    def __init__(self, documento):
        self.__cpf = documento
        self.__cpf_form = f"{self.__cpf[:3]}.{self.__cpf[3:6]}." \
                          f"{self.__cpf[6:9]}-{self.__cpf[9:]}"

    def __str__(self):
        return self.__cpf_form

    @property
    def cpf(self):
        return self.__cpf_form

    @property
    def validar(self):
        d1, d2 = 0, 0
        for i, j in enumerate(range(10, 1, -1)):
            d1 += int(self.__cpf[i]) * j
        d1 = 11 - (d1 % 11)
        d1 = 0 if d1 > 9 else d1
        for i, j in enumerate(range(11, 1, -1)):
            d2 += int(self.__cpf[i]) * j
        d2 = 11 - (d2 % 11)
        d2 = 0 if d2 > 9 else d2
        if f"{d1}{d2}" in self.__cpf:
            return True
        else:
            return False


class Documento(CPF):
    def __init__(self, documento):
        super().__init__(documento)
        self.__doc = documento

    @property
    def checar(self):
        if len(self.__doc) < 12:
            if CPF(self.__doc).validar:
                return True
            else:
                print(msg_doc)
                return False
        else:
            print(msg_doc)


msg_doc = """ErroDocumento ~01:
    Número do documento não é válido!"""
