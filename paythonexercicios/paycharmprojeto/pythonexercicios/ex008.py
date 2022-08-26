medida = float(input('uma distancia em metros:'))
cm = medida *100
mm = medida * 1000
dm = medida / 10
m = medida / 10
dom = medida / 10
hm = medida / 10
km = medida / 10

print('a media de {:.2f}mm corresponde a {:.2f}cm a {:.2f}mm a {:.2f}dm a {:.2f}m '
  'a {:.2f}dom a {:.2f}hm a {:.2f}km' . format( medida, cm, mm, dm, m, dom, hm, km))