def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao meu projeto Python 🚀"


def somar(a, b):
    return a + b


if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))

    print("\nVamos somar dois números:")
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    resultado = somar(n1, n2)
    print(f"Resultado: {resultado}")

    
