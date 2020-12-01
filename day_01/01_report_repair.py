import numpy as np

array = np.loadtxt('input.txt')

summe = np.add.outer(array, array)

result = np.where(summe == 2020)

listOfCoordinates= list(zip(result[0], result[1]))

for (m, n) in listOfCoordinates:
  m = array[m]
  n = array[n]
  sum = m+n
  multi = m*n

print(m)
print(n)
print('---')
print(sum)
print(multi)