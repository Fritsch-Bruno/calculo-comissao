nome_vendedor = input("Nome do vendedor: ")
salario_fixo = float(input("salario fixo: "))
total_mes = float(input("Total de vendas no mês: "))

valor_comissao = total_mes * 0.12
valor_bonus = total_mes * 0.05
valor_bruto = salario_fixo + valor_comissao + valor_bonus
valor_desc = valor_bruto * 0.08
valor_liquido = valor_bruto - valor_desc

print("valor da comissao de vendas: ", valor_comissao)
print("valor do bonus sobre as vendas: ", valor_bonus)
print("salario bruto: ", valor_bruto)
print("valor desconto: ", valor_desc)
print("valor liquido recebido: ", valor_liquido)
