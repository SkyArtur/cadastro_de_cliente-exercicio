"""
Módulo que armazena as mensagens impressas pelo programa.
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo principal
# ----------------------------------------------------------------------------------------------------------------------
abertura_do_programa = '''Exercício prático no aprendizado em Python.
Copyright (c) 2022 - Ponta Grossa/PR. 
Projeto Cadastro de Cliente.
Artur dos Santos Shon - EAD - UNINTER - 2021.'''
sistema_de_cadastro_de_clientes = '''------------------------------------------
     Sistema de Cadastro de Clientes
------------------------------------------'''
cadastro_do_cliente = '''------------------------------------------
            Cadastro do Cliente
------------------------------------------'''
operacoes_em_conta = '''------------------------------------------
           Operações em Conta
------------------------------------------'''
cliente_ja_cadastrado = '''ErroCadastro ~01:
    Cliente já cadastrado!'''
cliente_nao_encontrado = '''ErroCadastro ~03:
    Cliente não encontrado!'''
valor_excedeu_limite = '''ErroLimite ~01:
    O valor de saque excede seu limite disponível'''

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo registrador
# ----------------------------------------------------------------------------------------------------------------------
cpf_invalido = """ErroDocumento ~01:
    Número do CPF não é válido!
"""
cep_invalido = """ErroCep ~01:
    número de CEP inválido!
"""
endereco_encontrado = """MensagemCep ~01:
    Endereço encontrado!
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo gerenciador
# ----------------------------------------------------------------------------------------------------------------------
msg_gerenciador_01 = """MensagemGerente ~01:
    Arquivo do cliente criado com sucesso.
"""
msg_gerenciador_02 = """MensagemGerente ~02:
    Arquivo do cliente atualizado com sucesso.
"""
msg_gerenciador_03 = f"""MensagemGerente ~03:
    Arquivo não encontrado.
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo entrada
# ----------------------------------------------------------------------------------------------------------------------
digite_apenas_int = f'''ErroEntrada ~01:
    São aceitos apenas números inteiros.'''
digite_apenas_float = f'''ErroEntrada ~02:
    Não são aceitos letras ou caractéres especiais.
    Use o ponto(.) ao invés da vírgula(,) para separar
    casas decimais.'''
algo_errado_aconteceu = f'''ErroEntrada ~03:
    Parece que você digitou algo errado!'''
opcao_invalida = f'''InputMenuError ~01:
    Parece que você digitou uma opção inválida!!'''
entrada_invalida_cep = f'''InputCepError ~01:
    Parece que você digitou algo inválido.
    Por favor, digite apenas os números.'''
montar_menu_inicial = """Menu Inicial:
    [1] Cadastrar Novo Cliente
    [2] Operações em Conta
    [0] Encerrar"""
montar_menu_creditos = """Deseja definir os créditos do cliente?
    [1] Sim
    [2] Não"""
montar_menu_operacoes = """Qual operação deseja realizar?
    [1] Sacar
    [2] Depositar
    [3] Consultar extrato
    [4] Novo Crédito
    [0] Retornar"""
