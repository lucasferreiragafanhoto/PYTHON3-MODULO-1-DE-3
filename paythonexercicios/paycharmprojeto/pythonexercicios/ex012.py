preco = float(input('qual e o preco do produto? R$'))
novo = preco - ( preco * 5 / 100)
print('o produto que custav R${} na promoção com desconto de 5 % vai custar R${}' .format(preco, novo))