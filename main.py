
def bucketsort(a,n):
  max2 = max(a)
  b = [0.0] * (max2 + 1)
  for i in range(n):
    b[a[i]] += 1.0
  j = 0
  for i in range(max2 + 1):
    while b[i] > 0:
      a[j] = i
      j += 1
      b[i] -= 1

col = [79, 23, 12, 45, 32, 54, 21, 98]
length = len(col)
print(col)
bucketsort(col,length)
print(col)







