import random
import math
import numpy as np

def s_matmul(m1, m2):
    # Check input
    if m1.shape != m2.shape or m1.shape[0] != m1.shape[1]:
        raise ValueError("Matrices must be square and of equal size")
    
    if m1.shape[0] == 1:
        return m1 * m2
        
    elif m1.shape[0] > 1:
        # pad m1 and m2 to a power of 2
        n = m1.shape[0]
        pad_size = 2**math.ceil(math.log2(n)) - n
        m1 = np.pad(m1, [(0, pad_size), (0, pad_size)], 'constant')
        m2 = np.pad(m2, [(0, pad_size), (0, pad_size)], 'constant')

        # find quadrants of m1 and m2
        n = m1.shape[0]
        half = n // 2
        a = m1[:half, :half]
        b = m1[:half, half:]
        c = m1[half:, :half]
        d = m1[half:, half:]
        e = m2[:half, :half]
        f = m2[:half, half:]
        g = m2[half:, :half]
        h = m2[half:, half:]

        # compute components
        p1 = s_matmul(a, f - h)
        p2 = s_matmul(a + b,  h)
        p3 = s_matmul(c + d, e)
        p4 = s_matmul(d, g - e)
        p5 = s_matmul(a + d, e + h)
        p6 = s_matmul(b - d, g + h)
        p7 = s_matmul(a - c, e + f)

        #concatenate
        upper = np.concatenate((p5 + p4 - p2 + p6, p1 + p2), axis=1)
        lower = np.concatenate((p3 + p4, p1 + p5 - p3 - p7), axis=1)
        result = np.concatenate((upper, lower), axis=0)
        return result[:n - pad_size, :n - pad_size]

#example
n = 7
a = np.random.randint(10, size=(n, n))
b = np.random.randint(10, size=(n, n))

print("np.matmul:")
print(np.matmul(a, b))
print()
print("this method")
print(s_matmul(a, b))
