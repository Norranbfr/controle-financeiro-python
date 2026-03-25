def calcular_inss(salario_bruto):
    if salario_bruto <= 1621:
        desconto = salario_bruto * 0.075

    elif salario_bruto <= 2902.84:
        desconto = salario_bruto * 0.09

    elif salario_bruto <= 4354.27:
        desconto = salario_bruto * 0.12

    elif salario_bruto <= 8475.55:
        desconto = salario_bruto * 0.14

    else:
        desconto = 1186.57
    return desconto


def calcular_vt(salario_bruto):
    vt = salario_bruto * 0.06
    return vt


def calcular_irpf(base_irp):
    if base_irp <= 2428.80:
        imposto = 0

    elif base_irp <= 2826.65:
        imposto = (base_irp * 0.075) - 182.16

    elif base_irp <= 3751.05:
        imposto = (base_irp * 0.15) - 394.16

    elif base_irp <= 4664.68:
        imposto = (base_irp * 0.225) - 675.49

    else:
        imposto = (base_irp * 0.275) - 908.73
    return imposto


string = " Folha De Pagamento "
print(f"{string:=^54}")

while True:

    nome = input("digite o nome do funcionario (digite 0 para sair): ")
    if nome == "0":
        break
    while not nome or nome.isdigit():
        print("O nome é um número ou está vazio")
        nome = input("digite o nome do funcionario (digite 0 para sair): ")
        if nome == "0":
            exit()

    salario_bruto = float(input("digite o salario do funcionario: "))

    inss = calcular_inss(salario_bruto)
    base_irp = salario_bruto - inss

    irpf = calcular_irpf(base_irp)
    vale_transporte = salario_bruto * 0.06

    salario_liquido = salario_bruto - inss - irpf - vale_transporte
    print("=" * 30)
    print("Funcionario:", nome)
    print(f"Salario bruto: R$ {salario_bruto:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IRPF: R$ {irpf:.2f}")
    print(f"Vale transporte: R$  {vale_transporte:.2f}")
    print(f"Salario liquido: R$ {salario_liquido:.2f}")
    print("=" * 30)
    print()