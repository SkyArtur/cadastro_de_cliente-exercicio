from modulos.entrada import MeuInput
from modulos.validador import Documento
from modulos.menus import Menu


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
            limite = MeuInput('Limite: ', float).conteudo
        else:
            limite = 250
        disponivel = saldo + limite
        return [saldo, limite, disponivel]


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