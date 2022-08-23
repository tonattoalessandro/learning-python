price = float(input('Informe o preço do produto em R$'))

option = int(input("""Escolha uma opção de pagamento:
1 - À vista (Dinheiro ou Cheque) - \033[1;32m10% OFF\033[m
2 - À vista (Cartão de crédito) - \033[1;32m5% OFF\033[m
3 - 2x no cartão - Preço normal
4 - 3x ou mais no cartão - \033[1;31m20% DE JUROS\033[m
"""))

if option == 1:
    new_price = price - (price * 0.1)
    print(f'Com pagamento à vista em dinheiro ou cheque, o produto de R${price:.2f} sairá por {new_price:.2f} com 10% OFF.')
elif option == 2:
    new_price = price - (price * 0.05)
    print(f'Com pagamento à vista no cartão, o produto de R${price:.2f}, sairá por {new_price:.2f} com 5% OFF.')
elif option == 3:
    print(f'Com pagamento parcelado em 2x no cartão, o preço R${price:.2f} é mantido.')
elif option == 4:
    new_price = price + (price * 0.2)
    print(f'Com pagamento em 3x ou mais no cartão, o preço passa de R${price:.2f} para {new_price:.2f} com 20% de JUROS.')
else:
    print("OPÇÃO INVÁLIDA!")
