'''출력을 위한 숫자 서식화'''

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))

print(format(x, 'e'))
print(format(x, '0.2E'))

print('The value is {:0,.2f}'.format(x))

print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

swap_separators = { ord('.'):',', ord(','):'.'}
print(format(x, ',').translate(swap_separators))

print(ord('.'))
print(ord(','))

print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)
