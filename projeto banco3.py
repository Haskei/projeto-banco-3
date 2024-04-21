from abc import ABC, abstractproperty,abstractclassmethod
from datetime import datetime
import textwrap
i=0
nun_saque = int(0)
class Cliente:
    def __init__(self, endereço):
        self.endereco = endereço
        self.contas = []
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    def registrar_conta(self,conta):
        self.contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self,nome,nascimento,cpf,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
class Conta(self):
    def __init__(self,numero,cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "00001"
        self.cliente = cliente
        self.historico = Historico()
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(cliente,numero)
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    def sacar(self,din):
        saldo=self.saldo
        excesso=din>saldo
        if excesso:
            print("O valor excedeu o saldo")
        elif valor>0:
            self.saldo -= din
            print("saque de R$",din,"feito com sucesso")
            return True
        else:
            print("Valor dado não é valido")
            return False
    def deposito(self,depo):
        if depo>0:
            self._saldo += depo
            print("Deposito de R$",depo," feito com sucesso")
            return True
        else:
            print("O valor dado é invalido")
            return False
    class ContaCorrente(Conta):
        def __init__(self, numero,cliente):
            super().__init__(numero,cliente)
            self.limite = 500
            self.lim_saque = 3
        def sacar(self,din):
            numero_saques= len([transacao for transacao in self.historico.transacoes if transacao["tipo"]=Saque.__name__])
        excedeu_din = din>self.limite
        excedeu_saques = numero_saques>self.lim_saque
        if excedeu_din:
            print("Valor excedeu o limite")
        elif excedeu_saques:
            print("Excedeu o numero de saques diarios")
        else:
            super().sacar(valor)
        return False
    def __str__(self):
        return f"""\Agência:\t{self.agencia},
                    C/C:\t\t{self.numero}
                    Titular:\t{self.cliente.nome}"""
class Historico:
    def __init__(self):
        self._transacoes=[]
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor":transacao.valor,
                "data": datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            }
        )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self,conta):
        pass
class Saque(Transacao):
    def __init__(self,valor):
        self.valor=valor
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao= conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


while i != 1:
    clientes=[]
    contas=[]
    print("""
          Aperte S e enter parra fazer Saque
          Aperte C para criar Cliente
          Aperte L para Listar contas
          Aperto O para criar uma conta
          Aperte D e enter para fazer um deposito
          Aperte E e enter para ver o extrato
          aperte T e enterpara Terminar o programa
          Favor utilize letras maiusculas para a navegação deste menu""")
    menu=input()
    if menu=="S":
        sacar(clientes)
    elif menu=="C":
        criar_cliente(clientes)
    elif menu=="L":
        listar_contas(contas)
    elif menu=="L":
        listar_contas(contas)
    elif menu=="O":
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)
    elif menu=="D":
        depositar(clientes)
    elif menu=="E":
        exibir_extrato(clientes)
    elif menu=="T":
        print("Muito Obrigado, Volte sempre")
        i=1

