print(("컴프리헨션이 클 때는 제너레이터 표현식을 고려하자"))
it = (len(x) for x in open('my_file.txt'))
print(it)
print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)
print(next(roots))