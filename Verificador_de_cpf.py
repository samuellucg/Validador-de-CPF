import sys
cpf_digitado_pelo_Usuario = input("CPF: ")
cpf_enviado_pelo_Usuario = cpf_digitado_pelo_Usuario.replace("-","").replace(".","").replace(" ","")
flag_repeticao = cpf_enviado_pelo_Usuario[0] * len(cpf_enviado_pelo_Usuario)
if flag_repeticao == cpf_enviado_pelo_Usuario:
    print("Números inválidos\nTente novamente.")
    sys.exit()
lista_de_multiplicacao = []
multiplicacao = 10
for indices in cpf_enviado_pelo_Usuario:
    indices = int(indices)
    x = indices * multiplicacao
    lista_de_multiplicacao.append(x)
    multiplicacao -= 1
    if multiplicacao == 1:
        break
soma1 = sum(lista_de_multiplicacao)
multi_da_Soma = soma1 * 10
resto_da_Divisão = multi_da_Soma % 11
primeiro_digito = resto_da_Divisão if resto_da_Divisão <= 9 else 0
#
cpf_para_analise = cpf_enviado_pelo_Usuario[:10]
lista_para_Soma = []
contagem_regressiva = 11
resultado = 0
for i in cpf_para_analise:
    x = int(i) * contagem_regressiva
    lista_para_Soma.append(x)
    contagem_regressiva -= 1
soma = sum(lista_para_Soma) * 10
div = soma % 11
resultado = resultado if div > 9 else div
cpf_definitivo = (cpf_enviado_pelo_Usuario[:9]+str(primeiro_digito)+str(resultado))
if cpf_definitivo == cpf_enviado_pelo_Usuario:
    print(f"{cpf_definitivo} = Válido")
else:
    print("CPF INVÁLIDO")