class SISBANK:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo = 0
        self.__historico = ""
        self.__qsaque = 0
        self.__limite_saque_diario = 3

    def setDeposito(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__saldo += valor
            self.__historico += f"Depósito: R$ {valor} - Saldo atual: R$ {self.__saldo}\n"
        else:
            print("Valor inválido para depósito. Use um número inteiro positivo.")

    def getDeposito(self):
        return self.__saldo

    def setSaque(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            print("Valor inválido. Aceita somente valores positivos.")
        elif valor > self.__saldo:
            print("Saldo indisponível para saque.")
        elif self.__qsaque >= self.__limite_saque_diario:
            print("Você atingiu o limite de saques diários.")
        else:
            self.__saldo -= valor
            self.__qsaque += 1
            self.__historico += f"Saque: R$ {valor} - Saldo atual: R$ {self.__saldo}\n"

    def getSaque(self):
        return self.__saldo

    def getExtrato(self):
        extrato = f"Extrato do cliente: {self.__usuario}\n"
        extrato += self.__historico if self.__historico else "Nenhuma movimentação registrada.\n"
        extrato += f"Saldo final: R$ {self.__saldo}"
        return extrato


if __name__ == "__main__":
    bank = SISBANK("USER 1")
    op = ""
    menu = (
        "\n\t[d] - Depositar\n"
        "\t[s] - Sacar\n"
        "\t[e] - Extrato\n"
        "\t[q] - Sair\n"
    )

    while op != "q":
        print(menu)
        op = input("Escolha uma opção: ").lower()

        if op == "d":
            try:
                valor = int(input("Valor para depósito R$: "))
                bank.setDeposito(valor)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        elif op == "s":
            try:
                valor = int(input("Valor para saque R$: "))
                bank.setSaque(valor)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        elif op == "e":
            print(bank.getExtrato())
        elif op == "q":
            print("Encerrando o sistema. Obrigado por usar o SISBANK!")
        else:
            print("Opção inválida. Tente novamente.")