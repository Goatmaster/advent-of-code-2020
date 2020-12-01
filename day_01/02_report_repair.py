import numpy as np

array = np.loadtxt('input.txt')

summe = np.add.outer(array, array)

summe2 = np.add.outer(array, summe)

result = np.where(np.tril(summe2) == 2020)

listOfCoordinates = list(zip(result[0], result[1], result[2]))

for (m, n, o) in listOfCoordinates:
  m = array[m]
  n = array[n]
  o = array[o]
  sum = m+n+o
  multi = m*n*o

print(m)
print(n)
print(o)
print('---')
print(sum)
print(multi)