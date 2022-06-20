from os import mkdir
import time


class Relatorio:
    def __init__(self, data):
        self.__operacao = ('Sacar', 'Depositar', 'Criar', 'Consultar')
        self.__dados = data
        self.data = time.strftime('%d/%m/%Y - %H:%M', time.localtime())

    @property
    def rel_conta(self):
        relatorio = f"Nome: {self.__dados[0]} | CPF: {self.__dados[1]}\n" \
                    f"Endereço: {self.__dados[2]}\n" \
                    f"Saldo: R${self.__dados[3]:.2f} | Crédito: R${self.__dados[4]:.2f}\n" \
                    f"Disponível: R${self.__dados[5]:.2f}\n"
        return relatorio

    def rel_extrato(self, op, valor):
        relatorio = f"{self.__operacao[op]:>12} | {self.data} | {valor}"
        return relatorio


class Gerente(Relatorio):
    def __init__(self, user_dir, data=None):
        super().__init__(data)
        self.diretorio = f'./armazenamento/{user_dir}'
        self.arquivo_cliente = f'./armazenamento/{user_dir}/cliente.txt'
        self.arquivo_extrato = f'./armazenamento/{user_dir}/extrato.txt'
        try:
            mkdir('./armazenamento/')
        except FileExistsError:
            pass

    def procurar(self):
        try:
            arquivo = open(self.arquivo_cliente, 'rt')
            arquivo.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def visualizar_conta(self):
        try:
            arquivo = open(self.arquivo_cliente, 'rt')
            print(arquivo.read())
            arquivo.close()
        except FileNotFoundError:
            return msg3

    def visualizar_extrato(self):
        try:
            arquivo = open(self.arquivo_extrato, 'rt')
            print(arquivo.read())
            arquivo.close()
        except FileNotFoundError:
            return msg3

    def escrever_extrato(self, op, valor):
        try:
            mkdir(self.diretorio)
            arquivo = open(self.arquivo_extrato, 'wt+')
            arquivo.write(f"{super().rel_extrato(op, valor)}\n")
            arquivo.close()
            return msg1
        except FileExistsError:
            arquivo = open(self.arquivo_extrato, 'at')
            arquivo.write(f'{super().rel_extrato(op, valor)}\n')
            arquivo.close()
            return msg2

    def escrever_cliente(self):
        try:
            mkdir(self.diretorio)
            arquivo = open(self.arquivo_cliente, 'wt+')
            arquivo.write(f'{super().rel_conta}')
            arquivo.close()
            return msg1
        except FileExistsError:
            arquivo = open(self.arquivo_cliente, 'wt+')
            arquivo.write(f'{super().rel_conta}')
            arquivo.close()
            return msg2

    def extrair_dados(self):
        dados = list()
        try:
            arquivo = open(self.arquivo_cliente, 'rt')
            content = [user_data.strip() for user_data in arquivo.readlines()]
            dados.append(content[0][content[0].find('Nome:') + 6:content[0].find('|')].strip())
            dados.append(content[0][content[0].find('CPF:') + 5:].strip())
            dados.append(content[1][content[1].find('Endereço:') + 10:].strip())
            dados.append(float(content[2][content[2].find('Saldo:') + 9:content[2].find('|')].strip()))
            dados.append(float(content[2][content[2].find('Crédito:') + 11:].strip()))
            dados.append(float(content[3][content[3].find('Disponível:') + 14:].strip()))
            arquivo.close()
            return dados
        except FileNotFoundError:
            return msg3


msg1 = """MensagemGerente ~01:
    Arquivo do cliente criado com sucesso."""
msg2 = """MensagemGerente ~02:
    Arquivo do cliente atualizado com sucesso."""
msg3 = f"""MensagemGerente ~03:
    Arquivo não encontrado."""
