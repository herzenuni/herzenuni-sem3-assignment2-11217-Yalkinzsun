#---------------------
def gcd (a, b):
    while b:
        a, b = b, a % b
    return abs(a)
#---------------------

def nod(a, b):
    min = a if a < b else b
    largestFactor = 1
    for i in range(1, min + 1):
        if a % i == 0 and b % i == 0:
           largestFactor = i
    return largestFactor

def main():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    print('Нод для чисел a = {} и b = {} равен {}'.format(a,b, nod(a,b)))

main()
