real = float(input('quanto de dinheiro voçê tem na carteira?R$'))
dolar = real / 9.90
euro = real / 5.50
gbp = real / 6.50

print('com R${:.2f} voçê pode comprar Us${:.2f} o euro{:.2f} eo gbp{:.2f}'. format(real, dolar, euro, gbp))