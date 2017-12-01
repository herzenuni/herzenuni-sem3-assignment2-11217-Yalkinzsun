def buble_sort(a):
  n = len(a)
  m = n - 1
  while m > 0:
    for i in range(m):
      if (a[i] > a[i + 1]):
        x=a[i]
        a[i]=a[i + 1]
        a[i + 1]=x
    m = m - 1
  return a

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1],x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
    return first_part + second_part

#print(buble_sort([0,7,2,10,2,5]))
#print(quicksort([0,7,2,10,2,5]))

if __name__ == "__main__":
  import timeit
  data = [0,7,2,10,2,5]
  print(timeit.timeit("buble_sort(data)", setup="from __main__ import buble_sort, data", number = 10000))
  print(timeit.timeit("quicksort(data)", setup="from __main__ import quicksort, data", number = 10000))
