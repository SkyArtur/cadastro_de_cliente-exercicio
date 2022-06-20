from modulos.registrador import Conta, Cliente, CPF, RegistroConta, RegistroCliente
from modulos.entrada import Menu, MeuInput
from modulos.gerenciador import Gerente
from hashlib import md5
from time import sleep
from sys import exit
import os


def limpar_tela():
    os.system(command='cls') if os.name in ['nt', 'dos'] else os.system(command='clear')


def encerrar():
    print('Encerrando.......')
    sleep(1.5)
    return exit()


def cadastrar_cliente():
    limpar_tela()
    print(forma2)
    cliente = Cliente(RegistroCliente().cliente)
    nome_arquivo = md5(bytes(cliente.cpf, 'utf-8')).hexdigest()
    if Gerente(nome_arquivo).procurar_conta():
        print(msg1)
    else:
        conta = Conta(RegistroConta().conta)
        dados_principais = cliente.dados + conta.dados
        Gerente(nome_arquivo, dados_principais).escrever_extrato(op=0, valor=f"s R${conta.saldo:.2f}")
        print(Gerente(nome_arquivo, dados_principais).escrever_cliente())


def buscar_dados_do_cliente():
    limpar_tela()
    print(forma3)
    nome_arquivo = MeuInput('Digite o CPF: ').conteudo
    while not CPF(nome_arquivo).validar:
        print(msg2)
        nome_arquivo = MeuInput('Digite o CPF: ').conteudo
    else:
        nome_arquivo = md5(bytes(CPF(nome_arquivo).cpf, 'utf-8')).hexdigest()
        if Gerente(nome_arquivo).procurar_conta():
            limpar_tela()
            Gerente(nome_arquivo).escrever_extrato(op=1, valor="Consulta")
            Gerente(nome_arquivo).visualizar_conta()
        else:
            limpar_tela()
            print(msg3)


def operacao_em_conta():
    limpar_tela()
    print(forma4)
    nome_arquivo = MeuInput('Digite o CPF: ').conteudo
    if CPF(nome_arquivo).validar:
        nome_arquivo = md5(bytes(CPF(nome_arquivo).cpf, 'utf-8')).hexdigest()
        Gerente(nome_arquivo).visualizar_conta()
        dados_principais = Gerente(nome_arquivo).extrair_dados()
        cliente = Cliente(dados_principais[:3])
        conta = Conta(dados_principais[3:])
    else:
        print(msg2)
    while True:
        menu = Menu().menu_operacoes
        # ------------------------------------ Saque -----------------------------------------------------------
        if menu == 1:
            valor = MeuInput('Digite o valor: ', float).conteudo
            conta.sacar(valor)
            dados_principais = cliente.dados + conta.dados
            Gerente(nome_arquivo, dados_principais).escrever_extrato(op=3, valor=f"R${valor:.2f}")
            Gerente(nome_arquivo, dados_principais).escrever_cliente()
            Gerente(nome_arquivo).visualizar_conta()
        # ------------------------------------ Depósito --------------------------------------------------------
        elif menu == 2:
            valor = MeuInput('Digite o valor: ', float).conteudo
            conta.depositar(valor)
            dados_principais = cliente.dados + conta.dados
            Gerente(nome_arquivo, dados_principais).escrever_extrato(op=2, valor=f"R${valor:.2f}")
            Gerente(nome_arquivo, dados_principais).escrever_cliente()
            Gerente(nome_arquivo).visualizar_conta()
        # ------------------------------------ Extrato ---------------------------------------------------------
        elif menu == 3:
            Gerente(nome_arquivo).escrever_extrato(op=1, valor=f"Extrato")
            Gerente(nome_arquivo).visualizar_conta()
            Gerente(nome_arquivo).visualizar_extrato()
        # ------------------------------------ Retornar --------------------------------------------------------
        elif menu == 4:
            valor = MeuInput('Digite o novo limite: ', float).conteudo
            conta.credito = valor
            dados_principais = cliente.dados + conta.dados
            Gerente(nome_arquivo, dados_principais).escrever_extrato(op=4, valor=f"R${valor:.2f}")
            Gerente(nome_arquivo, dados_principais).escrever_cliente()
            Gerente(nome_arquivo).visualizar_conta()
        # ------------------------------------ Retornar --------------------------------------------------------
        else:
            limpar_tela()
            break


abertura = '''Exercício prático no aprendizado em Python.
Copyright (c) 2022 - Ponta Grossa/PR. 
Projeto Cadastro de Cliente.
Artur dos Santos Shon - EAD - UNINTER - 2021.'''
forma1 = '''------------------------------------------
     Sistema de Cadastro de Clientes
------------------------------------------'''
forma2 = '''------------------------------------------
            Cadastro do Cliente
------------------------------------------'''
forma3 = '''------------------------------------------
         Buscar Dados do Cliente
------------------------------------------'''
forma4 = '''------------------------------------------
           Operações em Conta
------------------------------------------'''
msg1 = '''ErroCadastro ~01:
    Cliente já cadastrado!'''
msg2 = '''ErroCadastro ~02:
    Número de CPF inválido!'''
msg3 = '''ErroCadastro ~03:
    Cliente não encontrado!'''

if __name__ == "__main__":
    limpar_tela()
    print(abertura)
    while True:
        # --------------------------------------------------------------------------------------------------------------
        print(forma1)
        menu = Menu().menu_inicial
        # ------------------------------------- Cadastrar Cliente ------------------------------------------------------
        if menu == 1:
            cadastrar_cliente()
        # ------------------------------------- Buscar Dados do Cliente ------------------------------------------------
        elif menu == 2:
            buscar_dados_do_cliente()
        # --------------------------------------- Operações em Conta ---------------------------------------------------
        elif menu == 3:
            operacao_em_conta()
        # ----------------------------------------- Encerrar Programa --------------------------------------------------
        else:
            encerrar()
