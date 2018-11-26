import bisect
a = ['a', 'o', 'i']
bisect.insort(a, 'd')
print a
print bisect.bisect(a, 'b')
