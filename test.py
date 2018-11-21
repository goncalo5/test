def test(x, y):
    return x + y * (y > 0)


a = [1]
soma = reduce(lambda x, y: x + y, a)
print soma
n_elem = reduce(lambda x, y: x + 1, [1] + a[1:])
print n_elem
media = float(soma) / n_elem
print media
diff = map(lambda x: x - media, a)
print diff
diff_square = map(lambda x: x ** 2, diff)
print diff_square
variancia = reduce(lambda x, y: x + y, diff_square)
print variancia
desvio_padrao = variancia ** .5
print 'desvio_padrao', desvio_padrao

print
media = float(sum(a)) / len(a)
print media


diff_square = map(lambda x: (x - media)**2, a)
desvio_padrao = sum(diff_square) ** .5
print desvio_padrao

variancia = 0
for value in a:
    variancia += (value - media)**2
print variancia ** 0.5
