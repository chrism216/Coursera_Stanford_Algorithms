import math

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    else:  
        numsize = int(max(math.log10(x), math.log10(y))) + 1 #size of biggest number
        n = math.ceil(numsize / 2)  #size of numbers to the right of the cut

        a, b = int(str(x).zfill(numsize)[:numsize//2]), int(str(x).zfill(numsize)[numsize//2:])
        c, d = int(str(y).zfill(numsize)[:numsize//2]), int(str(y).zfill(numsize)[numsize//2:])
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        third_term = karatsuba(a + b, c + d) - ac - bd
        result  = ac * (10 ** (n * 2)) + third_term * (10 ** n) + bd

        return result
        
print(karatsuba(a, b))
print(a*b)